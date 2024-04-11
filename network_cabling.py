import copy
import sys
import math

from math import ceil

n = int(input())
buildings_x = []
buildings_y = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    buildings_x.append(x)
    buildings_y.append(y)

base_lenght = max(buildings_x) - min(buildings_x)

temp_y = copy.deepcopy(buildings_y)
temp_y.sort()

y = temp_y[ceil(n / 2)]

length = base_lenght
for i in buildings_y:
    length += abs(i - y)

print("base_lenght", base_lenght, file=sys.stderr)
print("length", length, file=sys.stderr)

print(length)
