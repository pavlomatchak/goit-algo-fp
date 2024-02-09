import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges.setdefault(from_node, []).append((to_node, weight))
        self.edges.setdefault(to_node, []).append((from_node, weight))

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges.get(current_node, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

def shortest_paths(graph, start):
    return dijkstra(graph, start)

g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'D', 3)

start_vertex = 'D'
print(f"Shortest paths from vertex '{start_vertex}':")
for vertex, distance in shortest_paths(g, start_vertex).items():
    print(f"Distance to vertex '{vertex}': {distance}")
