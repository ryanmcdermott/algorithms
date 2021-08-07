from unittest import TestCase
from prime_sieve import prime_sieve


class PrimeSieveTest(TestCase):
    def test_primes(self):
        actual = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                  41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        expected = prime_sieve(100)
        assert actual == expected

    def test_no_primes(self):
        assert prime_sieve(1) == []

    def test_one_prime(self):
        assert prime_sieve(3) == [2]
