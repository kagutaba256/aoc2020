# sam little
# aoc day 6

with open('day6-input.txt', 'r') as f:
    data = f.read()

data = data.split('\n\n')

groups = []
for g in data:
    groups.append(g.split('\n'))

total = 0
for g in groups:
    sets = []
    for p in g:
        ys = set()
        for x in p:
            ys.add(x)
        sets.append(ys)

    i = sets.pop()
    for s in sets:
        i = i.intersection(s)

    total += len(i)

print(total)
