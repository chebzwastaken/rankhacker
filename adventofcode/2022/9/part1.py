import re 
import functools
import itertools
import collections
from collections import defaultdict
from collections import Counter
import sys 

inf = sys.argv[1] if len(sys.argv) > 1 else "input"
# pos holds all the positions H has to move
# e.g L5 means move left 5
pos = [(x) for x in open(inf).read().split('\n')]

# L: left, R: right, U: up, D: down



