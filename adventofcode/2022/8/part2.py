import re 
import functools
import itertools
import collections
from collections import defaultdict
from collections import Counter
import sys 

inf = sys.argv[1] if len(sys.argv) > 1 else "input"

ll = [[int(y) for y in list(x)] for x in open(inf).read().split('\n')]

def addt(x, y):
    if len(x) == 2: 
        return (x[0] + y[0], x[1] + y[1])

    return tuple(map(sum, zip(x, y)))


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def inr(pos, arr):
    return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

c = 0
for x in range(len(ll)):
    for y in range(len(ll[0])):
        height = ll[x][y]
        scoreany = 1
        for d in DIRS:
            score = 0 
            pos = addt(d, (x, y))
            while inr(pos, ll):
                score += 1
                if ll[pos[0]][pos[1]] >= height:
                    break
                pos = addt(d, pos)
            scoreany *= score
        if scoreany > c: 
            c = scoreany

print(c)
