from unittest import TestCase
from rabin_karp import rabin_karp


class RabinKarpTest(TestCase):
    def test_str_multiple_match(self):
        text = "thereisfooandbarandfooandbaz"
        pattern = "foo"
        assert rabin_karp(pattern, text) == [7, 19]

    def test_str_no_match(self):
        text = "foo"
        pattern = "bar"
        assert rabin_karp(pattern, text) == []
