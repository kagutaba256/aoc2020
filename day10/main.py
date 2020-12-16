# sam little
# aoc day 10

from itertools import permutations

with open('day10-input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')
data = list(map(int, data))

data.sort()

ones_count = 1
threes_count = 1

for idx, v in enumerate(data):
    if idx == 0:
        continue
    diff = v - data[idx-1]
    if diff == 1:
        ones_count += 1
    elif diff == 3:
        threes_count += 1

data.reverse()
data.append(0)
