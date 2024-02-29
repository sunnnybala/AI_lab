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
push_order = []
pop_order = []
def dfs(graph, node):
    push_order.append(node)
    print(node)
    visited.append(node)
    for i in graph.adj_list[node]:
        if i[0] not in visited:
            dfs(graph,i[0])
    pop_order.append(node)

def main():
    graph = Graph()
    graph.add_edge(5,0,1)
    graph.add_edge(5,2,1) 
    graph.add_edge(4,0,1) 
    graph.add_edge(4,1,1) 
    graph.add_edge(2,3,1) 
    graph.add_edge(3,1,1)
    print(graph.adj_list)
    graph.print_adj_list()
    dfs(graph, 5)
    for i in graph.adj_list:
        if i not in visited:
            dfs(graph, i)
    print("pop order is")
    print(pop_order)
    print("topo sort is")
    print(pop_order[::-1])

if __name__ == "__main__":
    main()
