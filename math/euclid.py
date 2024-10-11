def euclid(a, b):
    """Return the greatest common divisor of a and b."""
    if b == 0:
        return a
    # a // b -> whole number
    # a % b -> remainder
    return euclid(b, a % b)

print(euclid(123456789, 12345))