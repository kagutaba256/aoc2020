import random
import math

data = []
for x in range(250):
    data.append(abs(math.floor(random.gauss(1000, 100))))

with open('big-input.txt', 'w') as f:
    f.writelines("%s\n" % x for x in data)
