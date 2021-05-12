# coding: utf-8
import unittest

from pylambda.pair import PAIR, FIRST, SECOND


class TestPair(unittest.TestCase):
    def test_pair(self):
        p = PAIR(1)(2)
        self.assertEqual(FIRST(p), 1)
        self.assertEqual(SECOND(p), 2)


if __name__ == '__main__':
    unittest.main()
