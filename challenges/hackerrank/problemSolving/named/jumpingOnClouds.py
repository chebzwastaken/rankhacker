def jumpingOnClouds(c: list, k: int) -> int:
    energy = 100
    i = 0
    while True:
        i = (i + k) % len(c)
        energy -= 1
        if c[i] == 1:
            energy -= 2
        if i == 0:
            break
    return energy

print(jumpingOnClouds([0, 0, 1, 0], 2))