def gcd(a, b):
    """Greatest Common Divisor by Euclid"""
    a = abs(a)
    b = abs(b)
    if a == 0 and b == 0:
        return 1
    while b:
        a, b = b, a % b
    return a
