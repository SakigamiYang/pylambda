# coding: utf-8
import unittest

from pylambda.boolean import IDENTITY, TRUE, FALSE, NOT, AND, OR, XOR, IF


class TestBoolean(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(IDENTITY(1), 1)

    def test_bool(self):
        self.assertEqual(TRUE(1)(0), 1)
        self.assertEqual(FALSE(1)(0), 0)

    def test_not(self):
        self.assertEqual(NOT(TRUE), FALSE)
        self.assertEqual(NOT(FALSE), TRUE)

    def test_add(self):
        self.assertEqual(AND(TRUE)(TRUE), TRUE)
        self.assertEqual(AND(TRUE)(FALSE), FALSE)
        self.assertEqual(AND(FALSE)(TRUE), FALSE)
        self.assertEqual(AND(FALSE)(FALSE), FALSE)

    def test_or(self):
        self.assertEqual(OR(TRUE)(TRUE), TRUE)
        self.assertEqual(OR(TRUE)(FALSE), TRUE)
        self.assertEqual(OR(FALSE)(TRUE), TRUE)
        self.assertEqual(OR(FALSE)(FALSE), FALSE)

    def test_xor(self):
        self.assertEqual(XOR(TRUE)(TRUE), FALSE)
        self.assertEqual(XOR(TRUE)(FALSE), TRUE)
        self.assertEqual(XOR(FALSE)(TRUE), TRUE)
        self.assertEqual(XOR(FALSE)(FALSE), FALSE)

    def test_cond(self):
        self.assertEqual(IF(TRUE)(1)(0), 1)
        self.assertEqual(IF(FALSE)(1)(0), 0)


if __name__ == '__main__':
    unittest.main()
