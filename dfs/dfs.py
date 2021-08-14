def dfs_util(g, node, visited, result):
    result.append(node)
    visited.add(node)

    for neighbor in g[node]:
        if neighbor not in visited:
            dfs_util(g, neighbor, visited, result)

    return result


def dfs(g, source):
    return dfs_util(g, source, set(), [])
