graph = {
    2 : [1,3],
    3 : [8, 2],
    8 : [3,7],
    7 : [8],
    1 : [2,6],
    6 : [1,11],
    11 : [12,6],
    12 : [11,17],
    17 : [12,16],
    16 : [17],
    17 : [16,18],
    18 : [19,17],
    19 : [18,14],
    14 : [19,13,9],
    13 : [14],
    9 : [14,10],
    10 : [9,15,5],
    15: [10,20],
    20 : [15],
    5 : [4,10],
    4 : [5],
    


}

visited = set() 

def dfs(visited, graph, node):
    if node == 20:
        print(20)
        exit(0)
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    

dfs(visited, graph, 2)