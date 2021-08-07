from unittest import TestCase
from graph_color import graph_color


class GraphColorTest(TestCase):
    def test_cycle(self):
        graph = {
            1: [2, 3],
            2: [4, 5],
            3: [1],
            4: [],
            5: []
        }
        assert graph_color(graph) == True

    def test_no_cycle(self):
        graph = {
            1: [2, 3],
            2: [4],
            3: [5],
            4: [],
            5: []
        }

        assert graph_color(graph) == False
