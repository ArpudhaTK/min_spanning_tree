# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 05:55:40 2023

@author: arpud
"""

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find_set(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find_set(u)
        root_v = self.find_set(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                self.rank[root_v] += 1

def kruskal(graph, weights):
    vertices = set(v for edge in graph for v in edge)
    disjoint_set = DisjointSet(vertices)
    mst = []

    sorted_edges = sorted(graph, key=lambda edge: weights[edge])

    for edge in sorted_edges:
        u, v = edge
        if disjoint_set.find_set(u) != disjoint_set.find_set(v):
            mst.append(edge)
            disjoint_set.union(u, v)

    return mst


graph = {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C')}
weights = {('A', 'B'): 1, ('B', 'C'): 4, ('C', 'D'): 2, ('D', 'A'): 5, ('A', 'C'): 3}

minimum_spanning_tree = kruskal(graph, weights)
print("Minimum Spanning Tree (MST):", minimum_spanning_tree)
