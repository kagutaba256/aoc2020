# sam little
# aoc day 3

def count_trees(slope):
    count = 0
    trees_hit = 0
    idx = [0, 0]
    while count < len(data) - 1:
        idx[0] += slope[0]
        idx[1] += slope[1]
        if idx[1] > len(data):
            return trees_hit
        if data[idx[1]][idx[0] % len(data[0])] == '#':
            trees_hit += 1
        count += 1

    return trees_hit


with open('day3-input.txt', 'r') as f:
    data = f.read()

data = (data.split('\n'))

slopes = []
slopes.append([1, 1])
slopes.append([3, 1])
slopes.append([5, 1])
slopes.append([7, 1])
slopes.append([1, 2])

total = 1
for slope in slopes:
    total *= count_trees(slope)

print(total)
