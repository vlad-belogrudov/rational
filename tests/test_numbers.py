from decimal import DivisionByZero
import unittest
from rational.numbers import Rational


class TestCalc(unittest.TestCase):

    def test_string(self):
        x = Rational(2, 3)
        self.assertEqual(f"{x}", "2, 3")

    def test_repr(self):
        x = Rational(2, 3)
        self.assertEqual(repr(x), "Rational(2, 3)")

    def test_compare(self):
        x = Rational(2, 3)
        y = Rational(4, 6)
        self.assertTrue(x, y)

    def test_negative(self):
        x = Rational(-1, 1)
        self.assertEqual(x.a, -1)
        self.assertEqual(x.b, 1)

        y = Rational(1, -1)
        self.assertEqual(y.a, -1)
        self.assertEqual(y.b, 1)

    def test_normalize(self):
        numbers = {
          (4, 6): (2, 3),
          (6, 4): (3, 2),
          (-8, 2): (-4, 1),
          (8, -2): (-4, 1),
        }

        for a, b in numbers.items():
            with self.subTest(msg=f"{a} => {b}"):
                self.assertEqual(Rational(*a), Rational(*b))

    def test_zero_division(self):
        self.assertRaises(DivisionByZero, Rational, 1, 0)

    def test_non_integer(self):
        self.assertRaises(ValueError, Rational, 1.1, 2.2)

    def test_less(self):
        numbers = [
            Rational(0, 1),
            Rational(2, 3),
            Rational(-2, 3),
            Rational(3, 6),
            Rational(4, 6)]
        numbers.sort()
        dumped = " | ".join([str(n) for n in numbers])
        self.assertEqual(dumped, "-2, 3 | 0, 1 | 1, 2 | 2, 3 | 2, 3")

    def test_negate(self):
        x = Rational(1, 2)
        self.assertEqual(-x, Rational(-1, 2))

    def test_addition(self):
        x = Rational(1, 2)
        y = Rational(3, 4)
        self.assertEqual(x+y, Rational(5, 4))

    def test_subtraction(self):
        x = Rational(1, 2)
        y = Rational(3, 4)
        self.assertEqual(x-y, Rational(-1, 4))

    def test_multiplication(self):
        x = Rational(5, 6)
        y = Rational(3, 8)
        self.assertEqual(x*y, Rational(5, 16))

    def test_division(self):
        x = Rational(8, 17)
        y = Rational(-3, 34)
        self.assertEqual(x/y, Rational(-16, 3))
