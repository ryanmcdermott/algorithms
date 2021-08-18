from unittest import TestCase
from ford_fulkerson import ford_fulkerson


class FordFulkersonTest(TestCase):
    def test_graph_with_flow(self):
        # {
        #   node: {
        #     node: cost
        #   }
        # }
        graph = {
            0: {
                1: 16,
                2: 13
            },
            1: {
                2: 10,
                3: 12
            },
            2: {
                1: 4,
                4: 14
            },
            3: {
                2: 9,
                5: 20
            },
            4: {
                3: 7,
                5: 4
            },
            5: {}
        }

        assert ford_fulkerson(graph, 0, 5) == 23

    def test_empty_graph(self):
        graph = {0: {}}

        assert ford_fulkerson(graph, 0, 0) == 0
