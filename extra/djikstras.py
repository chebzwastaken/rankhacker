# djikstras algorithm
from random import randint

class djikstras:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.dist = {}
        self.prev = {}
        self.queue = []

    def run(self):
        self.dist[self.start] = 0 # distance from start to start is 0
        self.prev[self.start] = None # start has no previous node, holds all previous nodes
        self.queue.append(self.start) # nodes in queue to be used in graph[u][v] u: parent node and v: child node

        while len(self.queue) > 0:
            u = self.queue.pop(0)
            for v in self.graph[u]:
                alt = self.dist[u] + self.graph[u][v]
                if v not in self.dist or alt < self.dist[v]:
                    # this will update any existing distance to a smaller value or add a new node
                    # not sure what alt means, but it holds the sum of the distance from the start node to the current node and the 
                    self.dist[v] = alt
                    self.prev[v] = u
                    self.queue.append(v)

        return self.dist[self.end], self.get_path()
    
    def get_path(self):
        path = []
        u = self.end
        while u != self.start:
            path.append(u)
            u = self.prev[u]
        path.append(self.start)
        return path[::-1]

djikstras_graph = {
    'A': {'B': 7, 'C': 8},
    'B': {'A': 7, 'C': 2, 'D': 2},
    'C': {'A': 8, 'B': 2, 'D': 6, 'E': 5},
    'D': {'B': 2, 'C': 6, 'E': 3, 'F': 1},
    'E': {'C': 5, 'D': 3, 'F': 5},
    'F': {'D': 1, 'E': 5}
}

djikstras_start = 'A'
djikstras_end = 'F'

# def generate_graph(n):
#     graph = {}
#     for i in range(n):
#         graph[chr(65+i)] = {
#             chr(65+j): randint(1, n) for j in range(randint(1, n)) if j != i
#         }
#     return graph

# graph = generate_graph(6)
# print(graph)



djikstras_obj = djikstras(djikstras_graph, djikstras_start, djikstras_end)
print(djikstras_obj.run())

