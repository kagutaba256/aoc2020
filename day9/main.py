# sam little
# aoc day 9

import copy
import time

with open('day9-input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')

p_len = 25


def search_for_match(p, n):
    for i in p:
        for j in p[p.index(i):]:
            if int(i) + int(j) == int(n):
                return True
    return False


for idx, n in enumerate(data[p_len:]):
    p = data[idx:idx+p_len]
    p.sort()
    if not search_for_match(p, n):
        print(n)
        break
