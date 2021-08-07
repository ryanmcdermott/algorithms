from enum import Enum


class Colors(Enum):
    BLACK = 0
    GRAY = 1
    WHITE = 2


def dfs(v, graph, colors):
    colors[v] = Colors.GRAY

    for neighbor in graph[v]:
        if (colors[neighbor] == Colors.GRAY) or (colors[neighbor] == Colors.WHITE and dfs(neighbor, graph, colors)):
            return True

    colors[v] = Colors.BLACK


def graph_color(graph):
    colors = {v: Colors.WHITE for v in graph}

    for v in graph:
        if colors[v] == Colors.WHITE and dfs(v, graph, colors):
            return True

    return False
