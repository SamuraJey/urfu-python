from collections import deque

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
    
    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            for adjacent_vertex in self.vertices[vertex]:
                self.vertices[adjacent_vertex].remove(vertex)
            del self.vertices[vertex]
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].remove(vertex2)
            self.vertices[vertex2].remove(vertex1)
    
    def breadth_first_search(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for adjacent_vertex in self.vertices[vertex]:
                    if adjacent_vertex not in visited:
                        queue.append(adjacent_vertex)
    
    def depth_first_search(self, start_vertex, end_vertex=None):
        visited = set()
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                if vertex == end_vertex:
                    return True
                for adjacent_vertex in self.vertices[vertex]:
                    if adjacent_vertex not in visited:
                        stack.append(adjacent_vertex)
        return False
    
    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += f"{vertex}: "
            for adjacent_vertex in self.vertices[vertex]:
                result += f"{adjacent_vertex} "
            result += "\n"
        return result

# Create a new graph
graph = Graph()

# Add some vertices
le = "Только необычное привычно, только различия повторяются"
graph.add_vertex('Только')
graph.add_vertex('необычное')
graph.add_vertex('привычно')
graph.add_vertex('только')
graph.add_vertex('различия')
graph.add_vertex('повторяются')

# Add some edges
graph.add_edge('Только', 'необычное')
graph.add_edge('необычное', 'привычно')
graph.add_edge('привычно', 'только')
graph.add_edge('только', 'различия')
graph.add_edge('различия', 'повторяются')

# Perform a depth-first search starting at vertex 'только'
graph.depth_first_search('Только', 'различия')



