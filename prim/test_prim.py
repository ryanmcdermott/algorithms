from unittest import TestCase
from prim import prim


class PrimTest(TestCase):
    def test_small_graph(self):
        graph = {
            'A': {'B': 2, 'C': 3},
            'B': {'A': 2, 'C': 12, 'D': 10, 'E': 4},
            'C': {'A': 3, 'B': 12, 'F': 5},
            'D': {'B': 10, 'E': 7},
            'E': {'B': 4, 'D': 7, 'F': 16},
            'F': {'C': 5, 'E': 16, 'G': 9},
            'G': {'F': 9},
        }

        expected = ['D', 'E', 'B', 'A', 'C', 'F', 'G']
        assert prim(graph, 'D') == expected
