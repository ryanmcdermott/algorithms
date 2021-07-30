import unittest
from union_find import union_find


class UnionFindTest(unittest.TestCase):
    def test_union_find_small(self):
        graph = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        actual = union_find(graph)
        expected = [0, 0, 2]
        assert actual == expected
