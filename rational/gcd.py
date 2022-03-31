def gcd(a, b):
    """Greatest Common Divisor by Euclid"""
    a = abs(a)
    b = abs(b)
    if a == 0 and b == 0:
        return 1
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        a, b = b, a
    r = 1
    while r:
        r = a % b
        if r:
            a = b
            b = r
    return b
