import unittest
from kadane import kadane


class KadaneTest(unittest.TestCase):
    def test_max_subarray(self):
        arr = [-2, -3, 4, -1, -2, 1, 5, -3]
        res = kadane(arr)
        assert res == 7
