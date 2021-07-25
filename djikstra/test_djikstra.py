import unittest
from djikstra import djikstra


class DjikstraTest(unittest.TestCase):
    def test_connected_graph(self):
        graph = {
            'U': [('V', 2), ('W', 5), ('X', 1)],
            'V': [('U', 2), ('X', 2), ('W', 3)],
            'W': [('V', 3), ('U', 5), ('X', 3), ('Y', 1), ('Z', 5)],
            'X': [('U', 1), ('V', 2), ('W', 3), ('Y', 1)],
            'Y': [('X', 1), ('W', 1), ('Z', 1)],
            'Z': [('W', 5), ('Y', 1)],
        }

        actual = djikstra(graph, 'X')
        expected = {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
        assert actual == expected
