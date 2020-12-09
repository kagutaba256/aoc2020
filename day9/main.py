# sam little
# aoc day 9

with open('day9-input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')
data = list(map(int, data))

p_len = 25


def search_for_match(p, n):
    for i in p:
        for j in p[p.index(i):]:
            if i + j == n:
                return True
    return False


invalid_num = 0
for idx, n in enumerate(data[p_len:]):
    p = data[idx:idx+p_len]
    p.sort()
    if not search_for_match(p, n):
        invalid_num = n
        break

if invalid_num == 0:
    print('no invalid num')
    exit(0)

print(f'invalid num: \t{invalid_num}')


found = False
window_size = 1

while not found:
    window_size += 1
    for idx, n in enumerate(data):
        if(idx + window_size) < len(data):
            window = data[idx:idx+window_size]
            if sum(window) == invalid_num:
                window.sort()
                weakness = window[0] + window[window_size-1]
                print(f'weakness: \t{weakness}')
                exit(0)
