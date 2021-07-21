import unittest
from random import randrange
from bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):
    def test_arr_positives(self):
        arr = [randrange(0, 20) for i in range(0, 20)]
        expected = sorted(arr)
        actual = bubble_sort(arr)
        assert actual == expected

    def test_empty_arr(self):
        arr = []
        expected = sorted(arr)
        actual = bubble_sort(arr)
        assert actual == expected

    def test_single_item_arr(self):
        arr = [4]
        expected = sorted(arr)
        actual = bubble_sort(arr)
        assert actual == expected

    def test_arr_positives_negatives(self):
        arr = [randrange(-20, 20) for i in range(0, 20)]
        expected = sorted(arr)
        actual = bubble_sort(arr)
        assert actual == expected
