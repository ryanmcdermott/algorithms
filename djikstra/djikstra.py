import heapq


def djikstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while len(pq) > 0:
        distance, node = heapq.heappop(pq)

        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = distance + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances
