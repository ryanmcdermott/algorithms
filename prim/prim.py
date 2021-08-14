import heapq


def prim(graph, start):
    mst = [start]
    visited = set([start])
    edges = [(cost, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        _, destination = heapq.heappop(edges)
        if destination in visited:
            continue

        visited.add(destination)
        mst.append(destination)

        for neighbor, cost in graph[destination].items():
            if neighbor not in visited:
                heapq.heappush(edges, (cost, neighbor))

    return mst
