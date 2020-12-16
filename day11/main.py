# sam little
# aoc day 11

from pprint import PrettyPrinter
pp = PrettyPrinter()

with open('day11-input.txt', 'r') as f:
    data = f.read()

data = list(map(list, data.split('\n')))

pp.pprint(data)
print()


def count_adjacent_seats(data, i, j):
    count = 0

    # checks
    cu = i-1 >= 0
    cr = j+1 < len(row)
    cd = i+1 < len(data)
    cl = j-1 >= 0

    # up
    if cu:
        if data[i-1][j] == '#':
            count += 1

    # up right
    if cu and cr:
        if data[i-1][j+1] == '#':
            count += 1

    # right
    if cr:
        if data[i][j+1] == '#':
            count += 1

    # down right
    if cd and cr:
        if data[i+1][j+1] == '#':
            count += 1

    # down
    if cd:
        if data[i+1][j] == '#':
            count += 1

    # down left
    if cd and cl:
        if data[i+1][j-1] == '#':
            count += 1

    # left
    if cl:
        if data[i][j-1] == '#':
            count += 1

    # up left
    if cu and cl:
        if data[i-1][j-1] == '#':
            count += 1

    return count


def count_all_occupied(data):
    count = 0
    for row in data:
        for col in row:
            if col == '#':
                count += 1
    return count


while True:
    new_data = []
    for i, row in enumerate(data):
        new_data.append([])
        for j, seat in enumerate(row):
            if seat == '.':
                new_data[i] += '.'
                continue
            occupied_seat_count = count_adjacent_seats(data, i, j)

            if seat == 'L' and occupied_seat_count == 0:
                new_data[i] += '#'
            elif seat == '#' and occupied_seat_count >= 4:
                new_data[i] += 'L'
            else:
                new_data[i] += seat
    data = new_data
    pp.pprint(data)

    print(count_all_occupied(data))

    input()
