# coding: utf-8
import unittest

from pylambda.boolean import TRUE, FALSE, NOT
from pylambda.helpers import decode_number
from pylambda.natural import (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN,
                              SUCC, PRED, ADD, SUB, MUL, EXP,
                              ISZERO, GTE, LTE, GT, LT, EQ,
                              MIN, MAX)


class TestNatural(unittest.TestCase):
    def test_numbers(self):
        for f, n in zip([ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN], range(0, 11)):
            self.assertEqual(decode_number(f), n)

    def test_arithmetic(self):
        for f, n in zip([ZERO, ONE, TWO, THREE], [1, 2, 3, 4]):
            self.assertEqual(decode_number(SUCC(f)), n)
        for f, n in zip([ZERO, ONE, TWO, THREE], [0, 0, 1, 2]):
            self.assertEqual(decode_number(PRED(f)), n)
        for f1, f2, n in zip([ONE, TWO, THREE], [ONE, THREE, TWO], [2, 5, 5]):
            self.assertEqual(decode_number(ADD(f1)(f2)), n)
        for f1, f2, n in zip([ONE, TWO, FOUR], [ONE, ONE, TWO], [0, 1, 2]):
            self.assertEqual(decode_number(SUB(f1)(f2)), n)
        for f1, f2, n in zip([ONE, TWO, THREE], [ONE, THREE, TWO], [1, 6, 6]):
            self.assertEqual(decode_number(MUL(f1)(f2)), n)
        for f1, f2, n in zip([ONE, TWO, ONE, THREE, THREE], [ONE, ONE, TWO, TWO, THREE], [1, 2, 1, 9, 27]):
            self.assertEqual(decode_number(EXP(f1)(f2)), n)

    def test_validate(self):
        self.assertEqual(ISZERO(ZERO), TRUE)
        self.assertEqual(ISZERO(ONE), FALSE)
        for f1, f2, n in zip([ONE, TWO, THREE], [ONE, THREE, TWO], [TRUE, FALSE, TRUE]):
            self.assertEqual(GTE(f1)(f2), n)
            self.assertEqual(LT(f1)(f2), NOT(n))
        for f1, f2, n in zip([ONE, TWO, THREE], [ONE, THREE, TWO], [FALSE, FALSE, TRUE]):
            self.assertEqual(GT(f1)(f2), n)
            self.assertEqual(LTE(f1)(f2), NOT(n))
        for f1, f2, n in zip([ONE, TWO, THREE], [ONE, THREE, TWO], [TRUE, FALSE, FALSE]):
            self.assertEqual(EQ(f1)(f2), n)

    def test_advanced_arithmetic(self):
        self.assertEqual(MIN(ONE)(ONE), ONE)
        self.assertEqual(MIN(ONE)(TWO), ONE)
        self.assertEqual(MAX(FIVE)(THREE), FIVE)
        self.assertEqual(MAX(EIGHT)(EIGHT), EIGHT)


if __name__ == '__main__':
    unittest.main()
