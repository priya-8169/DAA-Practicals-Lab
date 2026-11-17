class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find_parent(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal(self):
        mst = []
        i, e = 0, 0
        # Sort edges by weight
        self.edges = sorted(self.edges, key=lambda item: item[2])
        
        parent = [node for node in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                mst.append([u, v, w])
                self.union(parent, rank, x, y)

        min_cost = sum(weight for _, _, weight in mst)
        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in mst:
            print(f"{u} -- {v} == {weight}")
        print(f"Minimum Spanning Tree Cost: {min_cost}")


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal()
