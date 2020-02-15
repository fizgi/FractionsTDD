""" Implement a test class for fractions to test
    addition, subtraction, multiplication, division,
    equal, not equal, less than, less than or equal to,
    greater thangreater than or equal to

    author: Fatih IZGI
    date: 11-Feb-2020
    version: python 3.6.9
"""

import unittest
from app import Fraction


class TestFraction(unittest.TestCase):
    """ test class Fraction """

    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f: Fraction = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.denom, 4)

    def test_init_exception(self):
        """ verify that ZeroDivisionError is raised when appropriate """
        with self.assertRaises(ZeroDivisionError):
            Fraction(3, 0) # trying to create a Fraction with 0 denomiator -> ZeroDivisionError

    def test_str(self):
        """ verify that __str__ works properly """
        f: Fraction = Fraction(1, 6)
        self.assertEqual(str(f), "1.0/6.0")

    def test_add(self):
        """ verify Fraction addition """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertEqual(f12, Fraction(1, 2))  # f12 should not have changed

    def test_add_3_operands(self):
        """ verify Fraction addition with more than two operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        self.assertTrue(f12 + f34 + f44 == Fraction(72, 32))

    def test_sub(self):
        """ verify Fraction substraction """
        f44: Fraction = Fraction(4, 4)
        f68: Fraction = Fraction(6, 8)
        self.assertEqual(f44 - f68, Fraction(8, 32))
        self.assertEqual(f44, Fraction(4, 4))  # f44 should not have changed

    def test_sub_3_operands(self):
        """ verify Fraction substraction with more than two operands """
        f41: Fraction = Fraction(4, 1)
        f55: Fraction = Fraction(5, 5)
        f32: Fraction = Fraction(3, 2)
        self.assertTrue(f41 - f55 - f32 == Fraction(15, 10))

    def test_mul(self):
        """ verify Fraction multiplication """
        f128: Fraction = Fraction(12, 8)
        f41: Fraction = Fraction(4, 1)
        self.assertEqual(f128 * f41, Fraction(48, 8))
        self.assertEqual(f128, Fraction(12, 8))  # f128 should not have changed

    def test_mul_3_operands(self):
        """ verify Fraction multiplication with more than two operands """
        f52: Fraction = Fraction(5, 2)
        f34: Fraction = Fraction(3, 4)
        f68: Fraction = Fraction(6, 8)
        self.assertTrue(f52 * f34 * f68 == Fraction(90, 64))

    def test_truediv(self):
        """ verify Fraction division """
        f32: Fraction = Fraction(3, 2)
        f912: Fraction = Fraction(9, 12)
        self.assertEqual(f32 / f912, Fraction(36, 18))
        self.assertEqual(f32, Fraction(3, 2))  # f32 should not have changed

    def test_truediv_3_operands(self):
        """ verify Fraction division with more than two operands """
        f34: Fraction = Fraction(3, 4)
        f55: Fraction = Fraction(5, 5)
        f912: Fraction = Fraction(9, 12)
        self.assertTrue(f34 / f55 / f912 == Fraction(180, 180))

    def test_later_zerodivision(self):
        """ verify ZeroDivisionError is raised when the second Fraction's result is 0 """
        with self.assertRaises(ZeroDivisionError):
            f34: Fraction = Fraction(3, 4)
            f05: Fraction = Fraction(0, 5)  # nominator is 0, no error will be raised
                                            # but this fraction will be the denominator of the first fraction
            result = f34 / f05 # Then this division will raise a ZeroDivisionError

    def test_eq(self):
        """ verify Fraction equation (eq) """
        f41: Fraction = Fraction(4, 1)
        f34: Fraction = Fraction(3, 4)
        f1510: Fraction = Fraction(15, 10)
        f128: Fraction = Fraction(12, 8)

        self.assertEqual(f41 == f34, False)
        self.assertEqual(f1510 == f128, True)

    def test_ne(self):
        """ verify Fraction equation (ne) """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f48: Fraction = Fraction(4, 8)
        f816: Fraction = Fraction(8, 16)

        self.assertEqual(f12 != f34, True)
        self.assertEqual(f48 != f816, False)

    def test_lt(self):
        """ verify Fraction less than """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f25: Fraction = Fraction(2, 5)
        f24: Fraction = Fraction(2, 4)
        fm13: Fraction = Fraction(-1, 3)
        f1m3: Fraction = Fraction(1, -3)
        f23: Fraction = Fraction(2, 3)

        self.assertEqual(f34 < f12, False)
        self.assertEqual(f25 < f24, True)
        self.assertEqual(fm13 < f23, True) # test for negative numbers
        self.assertEqual(f1m3 < f23, True)

    def test_le(self):
        """ verify Fraction less than or equal """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f25: Fraction = Fraction(2, 5)
        f24: Fraction = Fraction(2, 4)

        self.assertEqual(f25 <= f12, True)
        self.assertEqual(f12 <= f12, True)
        self.assertEqual(f34 <= f24, False)

    def test_gt(self):
        """ verify Fraction greater than """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f25: Fraction = Fraction(2, 5)
        f24: Fraction = Fraction(2, 4)

        self.assertEqual(f12 > f34, False)
        self.assertEqual(f24 > f25, True)

    def test_ge(self):
        """ verify Fraction greater than or equal """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f25: Fraction = Fraction(2, 5)
        f24: Fraction = Fraction(2, 4)

        self.assertEqual(f25 >= f12, False)
        self.assertEqual(f12 >= f12, True)
        self.assertEqual(f34 >= f24, True)

    def test_simplify(self):
        """ verify Fraction.simpligy() method"""
        self.assertTrue(str(Fraction(3, 10).simplify()) == str(Fraction(3, 10)))
        self.assertTrue(str(Fraction(9, 27).simplify()) == str(Fraction(1, 3)))
        self.assertTrue(str(Fraction(8, 12).simplify()) == str(Fraction(2, 3)))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
