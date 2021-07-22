from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


def bfs(g, source):
    res = []
    visited = set([source])
    q = deque([source])

    while len(q) > 0:
        node = q.popleft()
        res.append(node)

        for v in g.graph[node]:
            if v not in visited:
                visited.add(v)
                q.append(v)

    return res
