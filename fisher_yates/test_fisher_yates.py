from unittest import TestCase
from fisher_yates import fisher_yates


class FisherYates(TestCase):
    def test_shuffle(self):
        arr = [i for i in range(1, 25)]
        actual = fisher_yates(arr)
        expected = [22, 18, 19, 15, 12, 23, 1, 7, 11, 5, 3,
                    21, 4, 20, 6, 8, 10, 24, 16, 17, 9, 2, 14, 13]
        assert actual == expected
        assert set(actual) == set(arr)
