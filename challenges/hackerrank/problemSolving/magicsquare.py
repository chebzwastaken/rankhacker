import numpy as np
import sys
def generateAllMagicSquares():
    magic = [[8, 1, 6,], [3, 5, 7], [4, 9, 2]] 
    rotations = [np.rot90(magic, x) for x in range(4)]
    reflections = [np.flip(x, 1) for x in rotations]
    all_magic_3x3 = rotations + reflections

    return all_magic_3x3

def getCost(arr, magic_square):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(arr[i][j] - magic_square[i][j])
    return cost    

def formingMagicSquare(s):
    magic = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]

    min_cost = sys.maxsize

    for magic_square in magic:
        cost = getCost(s, magic_square)
        min_cost = min(min_cost, cost)
    return min_cost

print(formingMagicSquare([[8, 1, 6], [3, 5, 7], [4, 9, 7]]))
