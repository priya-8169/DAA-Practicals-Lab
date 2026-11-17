from itertools import permutations

def travelling_salesman(graph, start):
    vertices = [i for i in range(len(graph)) if i != start]
    min_cost = float('inf')
    best_path = []

    for perm in permutations(vertices):
        current_cost = 0
        k = start
        current_path = [start]

        for j in perm:
            current_cost += graph[k][j]
            k = j
            current_path.append(j)

        # Return to the starting city
        current_cost += graph[k][start]
        current_path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return min_cost, best_path


if __name__ == "__main__":
    # Distance matrix representing distances between 4 cities (0, 1, 2, 3)
    graph = [
        [0,  10, 15, 20],
        [10, 0,  35, 25],
        [15, 35, 0,  30],
        [20, 25, 30, 0]
    ]

    start_city = 0
    cost, path = travelling_salesman(graph, start_city)

    print("Optimal Path:", " -> ".join(map(str, path)))
    print("Minimum Travelling Cost:", cost)
