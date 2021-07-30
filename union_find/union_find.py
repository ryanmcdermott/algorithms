def union_find(graph):
    parents = [i for i in range(0, len(graph))]
    rank = [1] * len(graph)

    def find(i):
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]

        return i

    def union():
        for source_idx, neighbors in enumerate(graph):
            for neighbor, val in enumerate(neighbors):
                if val == 0:
                    continue

                x, y = find(source_idx), find(neighbor)

                if rank[y] > rank[x]:
                    parents[x] = y
                    rank[y] += rank[x]
                else:
                    parents[y] = x
                    rank[x] += rank[y]

    union()
    return parents
