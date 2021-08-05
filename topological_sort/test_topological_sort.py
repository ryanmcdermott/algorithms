import unittest
from topological_sort import topological_sort, Graph


class BFSTest(unittest.TestCase):
    def test_connected_graph(self):
        g = Graph()
        g.add_edge(5, 2)
        g.add_edge(5, 0)
        g.add_edge(4, 0)
        g.add_edge(4, 1)
        g.add_edge(2, 3)
        g.add_edge(3, 1)

        actual = topological_sort(g.graph)
        expected = [5, 4, 0, 2, 3, 1]

        assert actual == expected
