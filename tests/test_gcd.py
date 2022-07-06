import unittest

from ddt import data, ddt, unpack

from rational.gcd import gcd

@ddt
class TestGCD(unittest.TestCase):

    @data((0, 0, 1),
          (8, 0, 8),
          (0, 8, 8),
          (-1, 2, 1),
          (-8, 16, 8),
          (16, -8, 8),
          (36, 48, 12),
          (12345, 54321, 3),
    )
    @unpack
    def test_divisor(self, first, second, divisor):
        self.assertEqual(gcd(first, second), divisor)
