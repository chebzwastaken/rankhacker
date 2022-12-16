def circularArrayRotation(a:list, k:int, queries:list) -> list:
    return [a[(len(a) - k + q) % len(a)] for q in queries]
