import unittest

from rational.gcd import gcd


class TestGCD(unittest.TestCase):

    def test_divisor(self):
        numbers = {
            (0, 0): 1,
            (8, 0): 8,
            (0, 8): 8,
            (-1, 2): 1,
            (-8, 16): 8,
            (16, -8): 8,
            (36, 48): 12,
            (12345, 54321): 3,
        }

        for p, r in numbers.items():
            with self.subTest(msg=f"{p} => {r}"):
                self.assertEqual(gcd(*p), r)
