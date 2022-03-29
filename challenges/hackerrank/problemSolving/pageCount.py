def pageCount(n, p):
    return int(min(p//2, n//2 - p//2))

print(pageCount(6, 5))