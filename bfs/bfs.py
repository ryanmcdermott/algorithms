from collections import deque


def bfs(g, source):
    res = []
    visited = set([source])
    q = deque([source])

    while len(q) > 0:
        node = q.popleft()
        res.append(node)

        for v in g[node]:
            if v not in visited:
                visited.add(v)
                q.append(v)

    return res
