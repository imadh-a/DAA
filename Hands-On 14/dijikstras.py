import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    queue = [(0, start_node)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example graph
graph = {
    'A': {'B': 6, 'C': 2},
    'B': {'D': 1},
    'C': {'B': 3, 'D': 5},
    'D': {}
}

start_node = 'A'
print("Shortest distances from node", start_node, "using Dijkstra's algorithm:")
print(dijkstra(graph, start_node))

