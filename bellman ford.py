def bellman_ford(graph, source):
    # Create a distance array to store the shortest distance from the source node to all other nodes
    distance = [float('inf')] * len(graph)
    distance[source] = 0

    # Relax the edges repeatedly
    for _ in range(len(graph) - 1):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if graph[u][v] != 0:
                    distance[v] = min(distance[v], distance[u] + graph[u][v])

    # Check for negative weight cycles
    for u in range(len(graph)):
        for v in range(len(graph)):
            if graph[u][v] != 0 and distance[u] + graph[u][v] < distance[v]:
                raise ValueError("Negative weight cycle detected")

    return distance

# Example usage:
graph = [
    [0, -1, 4, 0, 0],
    [0, 0, 3, 2, 2],
    [0, 0, 0, 0, 0],
    [0, 1, 5, 0, 0],
    [0, 0, 0, -3, 0]
]
source = 0
distance = bellman_ford(graph, source)
print("Shortest distances from node", source, ":", distance)
