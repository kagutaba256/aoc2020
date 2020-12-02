# sam little
# aoc day 2

from os import closerange


with open('day2-input.txt', 'r') as f:
    data = f.read()

data = (data.split('\n'))
data.sort()

# process data
passwords = []
for x in data:
    password = {}
    tmp = x.split(' ')
    range_tmp = tmp[0].split('-')
    password['min'] = range_tmp[0]
    password['max'] = range_tmp[1]
    password['char'] = tmp[1].split(':')[0]
    password['string'] = tmp[2]
    passwords.append(password)


def part1():
    total = 0
    for p in passwords:
        c = p['string'].count(p['char'])
        if c >= int(p['min']) and c <= int(p['max']):
            total += 1

    print(total)


def part2():
    total = 0

    for p in passwords:
        b_min = p['string'][int(p['min'])-1] == p['char']
        b_max = p['string'][int(p['max'])-1] == p['char']
        if (b_min or b_max) and b_min != b_max:
            total += 1

    print(total)


part2()
