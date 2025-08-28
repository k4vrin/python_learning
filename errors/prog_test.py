import unittest
from errors import prog


class TestProg(unittest.TestCase):
    def test_count_c(self):
        self.assertEqual(prog.count_c("hello", "l"), 2)

    def test_count_c_empty(self):
        self.assertEqual(prog.count_c("", "a"), 0)

    def test_count_c_not_found(self):
        self.assertEqual(prog.count_c("hello", "z"), 0)