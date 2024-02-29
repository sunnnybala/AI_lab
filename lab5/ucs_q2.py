class Graph:
    def __init__(self):
        self.adj_list = {}
        self.no_v = set()
    
    def add_edge(self, node_from, node_to, weight):
        self.no_v.add(node_from)
        self.no_v.add(node_to)

        if node_from in self.adj_list:
            self.adj_list[node_from].append((node_to, weight))
        else:
            self.adj_list[node_from]=[]
            self.adj_list[node_from].append((node_to, weight))
        if node_to not in self.adj_list:
            self.adj_list[node_to]=[]

    def print_adj_list(self):
        for i in self.adj_list:
            for j in self.adj_list[i]:
                print(i,"->",j[0],j[1])


def ucs(goal, graph, start, answer):
    queue = []
    queue.append((0,start,[start]))
    queue = sorted(queue)
    while(queue):
        queue = sorted(queue)
        ele = queue.pop(0)

        if ele[1] in goal:
            if ele[1] in answer:
                if answer[ele[1]][0] > ele[0]:
                    answer[ele[1]]=(ele[0], ele[2].copy())
            else:
                answer[ele[1]]=(ele[0], ele[2].copy())
            print(ele[0], ele[2].copy())
            if len(answer) == len(goal):
                return answer
        
        
        for neighbour in graph.adj_list[ele[1]]:
            new_path = ele[2] + [neighbour[0]]
            new_cost = ele[0] + neighbour[1]
            neighbour_in_queue = False
            for i in queue:
                if neighbour[0] in i:
                    neighbour_in_queue = True
                    if new_cost<i[0]:
                        queue.remove(i)
                        queue.append((new_cost, neighbour[0], new_path))
                        queue = sorted(queue)
            if not neighbour_in_queue:
                queue.append((new_cost, neighbour[0], new_path))
                queue = sorted(queue)
            
def main():
    graph = Graph()
    graph.add_edge('S','A',5)
    graph.add_edge('S','B',9)
    graph.add_edge('S','D',6)
    graph.add_edge('A','B',3)
    graph.add_edge('A','G1',9)
    graph.add_edge('B','A',2)
    graph.add_edge('B','C',1)
    graph.add_edge('C','S',6)
    graph.add_edge('C','G2',5)
    graph.add_edge('C','F',2)
    graph.add_edge('D','C',2)
    graph.add_edge('D','E',2)
    graph.add_edge('E','G3',7)
    graph.add_edge('F','D',2)
    graph.add_edge('F','G3',8)
    goal = ['G1','G2','G3']
    answer = {}
    print("hello")
    answer = ucs(goal, graph, 'S', answer)
    print("hello")
    print(answer)

if __name__ == "__main__":
    main()