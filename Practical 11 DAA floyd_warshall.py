INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    # Initialize distance matrix with input graph values
    dist = [row[:] for row in graph]

    # Update shortest paths considering each vertex k as an intermediate vertex
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_solution(dist):
    print("Shortest distance matrix between every pair of vertices:")
    for row in dist:
        print("  ".join("INF" if val == INF else f"{val:3}" for val in row))


if __name__ == "__main__":
    # Adjacency matrix representation of the weighted directed graph
    graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]

    shortest_distances = floyd_warshall(graph)
    print_solution(shortest_distances)
