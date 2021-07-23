from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


def dfs_util(g, node, visited, result):
    result.append(node)
    visited.add(node)

    for neighbor in g.graph[node]:
        if neighbor not in visited:
            dfs_util(g, neighbor, visited, result)

    return result


def dfs(g, source):
    return dfs_util(g, source, set(), [])
