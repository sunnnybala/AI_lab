#this works for a relaxed version of cannibals, missionary problem where boat can drive by itself too

def eval(a,b):
    if(a<b):
        return -1000
    else:
        return a + b

def update_state(path, state):
    print("state:", state)
    print("path:", path)
    neighbour =[]
    a = state[0]
    b = state[1]
    c = state[2]
    d = state[3]

    if(c>=2):
        neighbour.append([a+2,b,c-2,d])
    if(d>=2):
        neighbour.append([a,b+2,c,d-2])
    if(a>=2):
        neighbour.append([a-2,b,c+2,d])
    if(b>=2):
        neighbour.append([a,b-2,c,d+2])

    if(c>=1 and d>=1):
        neighbour.append([a+1,b+1,c-1,d-1])
    if(a>=1 and b>=1):
        neighbour.append([a-1,b-1,c+1,d+1])
    current_eval = eval(a,b)
    max_eval = eval(a,b)
    best_update = [a,b,c,d]
    for i in neighbour:
        temp = eval(i[0],i[1])
        if(temp>max_eval):
            max_eval = temp
            best_update = i
    if(current_eval==max_eval):
        if(current_eval == 6):
            print("solution found")
            print(path)
            exit()
        if(best_update == state):
            print("stuck")
            exit()
        else:
            print("plateu")
    path.append(best_update)
    state[0] = best_update[0]
    state[1] = best_update[1]
    state[2] = best_update[2]
    state[3] = best_update[3]


def main():
    state = [0,0,3,3]
    path = []
    path.append(state.copy())
    i=0
    while(True):
        update_state(path, state)
        i=i+1
        print("iteration",i)

if __name__ == "__main__":
    main()
