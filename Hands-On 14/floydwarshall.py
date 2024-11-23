def floyd_warshall(graph):
    vertices = list(graph.keys())
    num_vertices = len(vertices)
    dist = {i: {j: float('inf') for j in vertices} for i in vertices}

    for i in vertices:
        dist[i][i] = 0

    for u in graph:
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example graph
graph = {
    'A': {'B': 3, 'C': 7},
    'B': {'A': 8, 'C': 2},
    'C': {'A': 5, 'B': 1}
}

print("Shortest distances between all pairs of nodes using Floyd-Warshall algorithm:")
print(floyd_warshall(graph))


