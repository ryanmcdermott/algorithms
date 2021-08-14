import unittest
from dfs import dfs as traverse


class BFSTest(unittest.TestCase):
    def test_connected_graph(self):
        g = {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: []
        }

        actual = traverse(g, 0)
        expected = [0, 1, 2, 3]

        assert actual == expected
