def permutationEquation(p):
    return [p.index(p.index(x + 1) + 1) + 1 for x in range(len(p))]

print(permutationEquation([5, 2, 1, 3, 4]))