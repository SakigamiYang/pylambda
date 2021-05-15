# coding: utf-8
import unittest

from pylambda.helpers import decode_number
from pylambda.natural import ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN
from pylambda.recursive import FACT, FIB


class TestRecursive(unittest.TestCase):
    def test_recursive(self):
        for f, n in zip([ZERO, ONE, TWO, THREE, FOUR], [1, 1, 2, 6, 24]):
            self.assertEqual(decode_number(FACT(f)), n)
        for f, n in zip([ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN],
                        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]):
            self.assertEqual(decode_number(FIB(f)), n)


if __name__ == '__main__':
    unittest.main()
