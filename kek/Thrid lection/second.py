class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
def printGraph(graph):
    for src in range(len(graph.adjList)):
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest}) ', end='')
        print()
 
 
if __name__ == '__main__':
    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
    le = "Только необычное привычно, только различия повторяются"
    n = 6
    graph = Graph(edges, n)
    printGraph(graph)