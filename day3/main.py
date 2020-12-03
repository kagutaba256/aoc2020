# sam little
# aoc day 2

import numpy as np


def count_trees(slope):
    count = 0
    trees_hit = 0
    idx = np.array([0, 0])
    while count < len(data) - 1:
        idx += slope
        if idx[1] > len(data):
            return trees_hit
        if data[idx[1]][idx[0] % len(data[0])] == '#':
            trees_hit += 1
        count += 1

    return trees_hit


with open('day3-input.txt', 'r') as f:
    data = f.read()

data = (data.split('\n'))

slope1 = np.array([1, 1])
slope2 = np.array([3, 1])
slope3 = np.array([5, 1])
slope4 = np.array([7, 1])
slope5 = np.array([1, 2])

slopes = []
slopes.append(slope1)
slopes.append(slope2)
slopes.append(slope3)
slopes.append(slope4)
slopes.append(slope5)

total = 1
for slope in slopes:
    total *= count_trees(slope)

print(total)
