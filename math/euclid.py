def euclid(a, b):
    """Return the greatest common divisor of a and b."""
    v = []
    if b == 0:
        return a
    v.append([a // b, a % b])
    # a // b -> whole number
    # a % b -> remainder
    return euclid(b, a % b)

print(euclid(123456789, 12345))