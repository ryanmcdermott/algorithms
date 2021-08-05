class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append(v)


def do_topological_sort(node, stack, visited, graph):
    visited.add(node)
    if node in graph:
        for neighbor in graph[node]:
            if neighbor not in visited:
                do_topological_sort(neighbor, stack, visited, graph)

    stack.append(node)


def topological_sort(graph):
    stack = []
    visited = set()

    keys = sorted(list(graph.keys()))
    for node in keys:
        if node not in visited:
            do_topological_sort(node, stack, visited, graph)

    return stack[::-1]
