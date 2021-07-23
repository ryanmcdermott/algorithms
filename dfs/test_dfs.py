import unittest
from dfs import dfs as traverse, Graph


class BFSTest(unittest.TestCase):
    def test_connected_graph(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)

        actual = traverse(g, 0)
        expected = [0, 1, 2, 3]

        assert actual == expected
