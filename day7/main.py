# sam little
# aoc day 7
with open('day7-input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')
b = {}
for d in data:
    temp = d.replace(' ', '').replace('.', '').replace('bags', 'bag')
    x = temp.split('contain')
    y = x[1].split(',')
    counts = []
    for a in y:
        t = {}
        count = a[0]
        if count != 'n':
            t['count'] = int(count)
            t['name'] = a[1:]
            counts.append(t)

    z = x[:1]
    z.append(counts)
    b[z[0]] = z[1]


def open_bag_count_kind(bag_name, kind):
    for bag in b[bag_name]:
        if bag['name'] == kind:
            return 1
        x = open_bag_count_kind(bag['name'], kind)
        if x == 1:
            return 1
    return 0


count = 0
for entry in b:
    count += open_bag_count_kind(entry, 'shinygoldbag')

print(count)
