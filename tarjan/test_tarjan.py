from unittest import TestCase
from tarjan import tarjan


class TarjanTest(TestCase):
    def test_small_graph(self):
        graph = {
            0: [2, 3],
            1: [0],
            2: [1],
            3: [4],
            4: []
        }

        assert tarjan(graph) == [[4], [3], [1, 2, 0]]
