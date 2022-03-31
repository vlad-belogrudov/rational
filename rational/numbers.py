from decimal import DivisionByZero
from . import gcd


class Rational:
    def __init__(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError
        if b == 0:
            raise DivisionByZero
        self.a = a
        self.b = b
        self.normalize()

    def normalize(self):
        if self.b < 0:
            self.b = - self.b
            self.a = - self.a
        divisor = gcd.gcd(self.a, self.b)
        self.a //= divisor
        self.b //= divisor

    def __str__(self):
        return f"{self.a}, {self.b}"

    def __repr__(self):
        return f"Rational({self.a}, {self.b})"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __neg__(self):
        return Rational(-self.a, self.b)

    def __add__(self, other):
        return Rational(self.a * other.b + other.a * self.b, self.b * other.b)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Rational(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Rational(self.a * other.b, self.b * other.a)
