import unittest
from bfs import bfs as traverse


class BFSTest(unittest.TestCase):
    def test_connected_graph(self):
        g = {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: []
        }

        actual = traverse(g, 2)
        expected = [2, 0, 3, 1]

        assert actual == expected
