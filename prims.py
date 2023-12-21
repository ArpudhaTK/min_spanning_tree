def prim_mst(graph, weights, r):
    n = len(graph)
    key = [float('inf')] * n
    pi = [None] * n
    visited = [False] * n

    key[r] = 0

    for _ in range(n):
        u = min((v for v in range(n) if not visited[v]), key=lambda x: key[x])
        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v] and weight < key[v]:
                pi[v] = u
                key[v] = weight

    return pi, key


graph = {
    0: [(1, 2), (2, 1)],
    1: [(0, 2), (2, 3), (3, 10)],
    2: [(0, 1), (1, 3)],
    3: [(1, 10), (2, 5)]
}

weights = {(u, v): weight for u, edges in graph.items() for v, weight in edges}

r = 1  
pi, key = prim_mst(graph, weights, r)

print("Parent pointers:", pi)
print("Key values:", key)
