import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_vertex, parent_vertex)
    mst_edges = []
    total_cost = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        total_cost += weight

        if parent is not None:
            mst_edges.append((parent, u, weight))

        for v, edge_weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (edge_weight, v, u))

    return mst_edges, total_cost


if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1), ('E', 4)],
        'C': [('A', 3), ('B', 1), ('F', 5)],
        'D': [('B', 1), ('E', 1)],
        'E': [('B', 4), ('D', 1), ('F', 1)],
        'F': [('C', 5), ('E', 1)]
    }

    mst, cost = prim_mst(graph, 'A')

    print("Edges in Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print(f"Total Minimum Cost: {cost}")
