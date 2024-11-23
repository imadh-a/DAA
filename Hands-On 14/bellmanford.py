def bellman_ford(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

    for u in graph:
        for v, w in graph[u].items():
            if distances[u] + w < distances[v]:
                return "Negative cycle detected"

    return distances

# Example graph
graph = {
    'A': {'B': 6, 'C': 2},
    'B': {'D': 1},
    'C': {'B': -2, 'D': 5},
    'D': {}
}

start_node = 'A'
print("Shortest distances from node", start_node, "using Bellman-Ford algorithm:")
print(bellman_ford(graph, start_node))



