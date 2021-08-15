from collections import deque


def ford_fulkerson(graph, source, sink):
    parent = dict().fromkeys(graph, -1)
    max_flow = 0

    def bfs(start, end):
        q = deque([start])
        visited = set([start])
        while q:
            u = q.popleft()
            for node, cost in graph[u].items():
                if node in visited or cost <= 0:
                    continue

                visited.add(node)
                q.append(node)
                parent[node] = u
                if node == end:
                    return True

        return False

    while bfs(source, sink):
        path_flow = float('inf')
        v = sink
        while v != source:
            path_flow = min(path_flow, graph[parent[v]][v])
            v = parent[v]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            if graph[u].get(v):
                graph[u][v] -= path_flow
            else:
                graph[u][v] = -path_flow

            if graph[v].get(u):
                graph[v][u] += path_flow
            else:
                graph[v][u] = path_flow

            v = parent[v]

    return max_flow
