# sam little
# aoc day 4

with open('day5-input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')


def make_bin(s):
    s = s.replace('F', '0')
    s = s.replace('B', '1')
    s = s.replace('L', '0')
    s = s.replace('R', '1')

    front = s[:7]
    back = s[7:]

    r_n = int(front, 2)
    c_n = int(back, 2)

    sid = r_n * 8 + c_n

    n = int(s, 2)

    return(r_n, c_n, sid, n)


n_list = []

for d in data:
    res = make_bin(d)
    n_list.append(res[3])

num_list = [x for x in range(48, 875)]

for n in num_list:
    if n not in n_list:
        print(n)
