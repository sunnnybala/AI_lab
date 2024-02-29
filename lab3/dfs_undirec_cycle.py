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

visited = []
present_path = []

def dfs(graph, node, flag):
    print(node)
    visited.append(node)
    present_path.append(node)
    for i in graph.adj_list[node]:
        if i[0] not in visited:
            dfs(graph,i[0],flag)
        else:
            if(i[0] in present_path):
                flag[0] = flag[0]+1
    present_path.pop()

def main():
    flag = [0]
    graph = Graph()
    graph.add_edge(0,1,1)
    graph.add_edge(0,2,1)
    graph.add_edge(1,2,1) 
    graph.add_edge(2,0,1) 
    graph.add_edge(2,3,1) 
    graph.add_edge(3,3,1)
    print(graph.adj_list)
    graph.print_adj_list()
    for i in graph.adj_list:
        if i not in visited:
            dfs(graph, i,flag)
    print("flag :",flag)
    if flag[0] !=0:
        print("graph is cyclic")

if __name__ == "__main__":
    main()