from unittest import TestCase
from gcd import gcd


class GcdTest(TestCase):
    def test_gcd(self):
        assert gcd(16, 4) == 4
        assert gcd(17, 5) == 1
        assert gcd(30, 20) == 10
        assert gcd(10, 0) == 10
