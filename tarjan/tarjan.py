class Tarjan:
    def __init__(self, graph):
        self.graph = graph
        self.id = 0
        self.disc = dict.fromkeys(self.graph, -1)
        self.low = dict.fromkeys(self.graph, -1)
        self.visited = set()
        self.stack = []
        self.res = []

    def connect(self, u):
        self.disc[u] = self.id
        self.low[u] = self.id
        self.id += 1

        self.visited.add(u)
        self.stack.append(u)

        for v in self.graph[u]:
            if self.disc[v] == -1:
                self.connect(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif u in self.visited:
                self.low[u] = min(self.low[u], self.disc[v])

        w = -1
        if self.low[u] == self.disc[u]:
            temp = []
            while w != u:
                w = self.stack.pop()
                temp.append(w)
                self.visited.remove(w)

            self.res.append(temp)

    def scc(self):
        for u in self.graph:
            if self.disc[u] == -1:
                self.connect(u)

        return self.res


def tarjan(graph):
    t = Tarjan(graph)
    return t.scc()
