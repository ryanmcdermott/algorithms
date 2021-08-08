from unittest import TestCase
from totient import totient


class TotientTest(TestCase):
    def test_totient(self):
        assert totient(1) == 1
        assert totient(2) == 1
        assert totient(3) == 2
        assert totient(4) == 2
        assert totient(5) == 4
        assert totient(6) == 2
        assert totient(7) == 6
        assert totient(8) == 4
        assert totient(9) == 6
        assert totient(10) == 4
