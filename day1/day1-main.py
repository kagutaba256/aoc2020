# sam little 20201001
# advent of code day 1

with open('big-input.txt', 'r') as f:
    data = f.read()

data = (data.split('\n'))
data = [int(x) for x in data]
data.sort()


def part1():
    for x in data:
        for y in data[:data.index(x)]:
            if x + y == 2020:
                return f"x:\t{x}\ny:\t{y}\nsum:\t{x * y}"
    return "no matches found"


def part2():
    for x in data:
        for y in data[:data.index(x)]:
            for z in data[:data.index(y)]:
                if x + y + z == 2020:
                    return f"x:\t{x}\ny:\t{y}\nz:\t{z}\nsum:\t{x * y * z}"
    return "no matches found"


result = part2()
print(result)
