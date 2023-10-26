# Класс для представления graphического объекта
class Graph:
    # Конструктор
    def __init__(self, edges, n):
        # выделяет память для списка смежности
        self.adjList = [[] for _ in range(n)]
 
        # добавляет ребра в ориентированный graph
        for (src, dest) in edges:
            # выделяет узел в списке смежности от src до dest
            self.adjList[src].append(dest)
 
 
# Функция печати представления списка смежности Graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # вывести текущую вершину и все соседние с ней вершины
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest}) ', end='')
        print()
 
 
if __name__ == '__main__':
 
    # Вход #: ребра в ориентированном Graph
    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
    le = "Только необычное привычно, только различия повторяются"
 
    # Количество вершин (от 0 до 5)
    n = 6
 
    # построить graph из заданного списка ребер
    graph = Graph(edges, n)
 
    # печатать представление списка смежности Graph
    printGraph(graph)