from bisect import bisect_left
import unittest
from binary_search import binary_search


class BinarySearchTest(unittest.TestCase):
    def test_small_list(self):
        arr = [2, 11, 23, 26, 30, 31, 37, 48, 50, 52,
               58, 63, 66, 77, 80, 82, 88, 95, 96, 97]
        actual = bisect_left(arr, 31)
        print(actual)
        print(arr)

        assert actual == binary_search(arr, 31)

    def test_empty_arr(self):
        assert binary_search([], 42) == -1

    def test_single_item_present(self):
        assert binary_search([12], 12) == 0
