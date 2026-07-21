import heapq


class DisjointSet:
    """Disjoint Set (Union-Find) for Kruskal's Algorithm"""

    def __init__(self, vertices):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # ----------------------------------------------------
    # Kruskal's Algorithm
    # ----------------------------------------------------
    def kruskal(self):
        ds = DisjointSet(self.V)

        mst = []
        total_weight = 0

        edges = sorted(self.edges)

        for weight, u, v in edges:

            if ds.union(u, v):
                mst.append((u, v, weight))
                total_weight += weight

                if len(mst) == self.V - 1:
                    break

        return mst, total_weight

    # ----------------------------------------------------
    # Prim's Algorithm
    # ----------------------------------------------------
    def prim(self, start=0):

        visited = [False] * self.V

        min_heap = []
        heapq.heappush(min_heap, (0, start, -1))

        mst = []
        total_weight = 0

        while min_heap and len(mst) < self.V:

            weight, vertex, parent = heapq.heappop(min_heap)

            if visited[vertex]:
                continue

            visited[vertex] = True

            if parent != -1:
                mst.append((parent, vertex, weight))
                total_weight += weight

            for neighbor, edge_weight in self.adj[vertex]:
                if not visited[neighbor]:
                    heapq.heappush(
                        min_heap,
                        (edge_weight, neighbor, vertex)
                    )

        return mst, total_weight


def print_mst(title, mst, total_weight):
    print("=" * 55)
    print(title)
    print("=" * 55)

    print(f"\n{'Edge':<15}Weight")
    print("-" * 25)

    for u, v, w in mst:
        print(f"{u} -- {v:<8}{w}")

    print("-" * 25)
    print(f"Total Weight = {total_weight}\n")


def complexity_analysis():
    print("=" * 55)
    print("Time Complexity Analysis")
    print("=" * 55)

    print("\nKruskal's Algorithm")
    print("--------------------")
    print("Sorting Edges      : O(E log E)")
    print("Union-Find         : O(E α(V))")
    print("Overall Complexity : O(E log E)")

    print("\nPrim's Algorithm")
    print("----------------")
    print("Using Min Heap     : O(E log V)")


def main():

    graph = Graph(7)

    # Graph with 7 vertices and 9 edges

    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 3, 9)
    graph.add_edge(1, 4, 7)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 15)
    graph.add_edge(3, 5, 6)
    graph.add_edge(4, 6, 9)

    # -----------------------------
    # Kruskal
    # -----------------------------

    mst_kruskal, weight_kruskal = graph.kruskal()

    print_mst(
        "Kruskal's Minimum Spanning Tree",
        mst_kruskal,
        weight_kruskal
    )

    # -----------------------------
    # Prim
    # -----------------------------

    mst_prim, weight_prim = graph.prim()

    print_mst(
        "Prim's Minimum Spanning Tree",
        mst_prim,
        weight_prim
    )

    # -----------------------------
    # Verification
    # -----------------------------

    print("=" * 55)
    print("Verification")
    print("=" * 55)

    if weight_kruskal == weight_prim:
        print("\nBoth algorithms produced the SAME MST weight.")
    else:
        print("\nThe MST weights are different.")

    print(f"\nKruskal Weight : {weight_kruskal}")
    print(f"Prim Weight    : {weight_prim}")

    complexity_analysis()


if __name__ == "__main__":
    main()
