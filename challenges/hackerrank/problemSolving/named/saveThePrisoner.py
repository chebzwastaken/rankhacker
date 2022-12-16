import math
import os
import random
import re
import sys

def rsaveThePrisoner(n, m, s):
    print(n, m, s)
    if m != 1 and s == n:
        return saveThePrisoner(n, m - 1, 1)
    if m == 1: 
        return s
    return saveThePrisoner(n, m - 1, s + 1)

def saveThePrisoner(n, m, s):
    return (s + m - 2) % n + 1

inf = sys.argv[1] if len(sys.argv) > 1 else "input"

for i, line in enumerate(open(inf).readlines()):
    # each line is a test case
    if i == 0:
        continue
    n, m, s = [int(x) for x in line.split()]
    print(saveThePrisoner(n, m, s))
