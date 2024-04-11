import sys
import math

# def isMaxRel(list: [], pos: int) -> bool :
#     if pos == 0:
#         return True
#     elif pos == len(list) - 1:
#         return False
#     elif list[pos] > list[pos + 1] and list[pos] > list[pos - 1]:
#         return True
#
#     return False
#
# def isMinRel(list: [], pos: int) -> bool :
#     if pos == 0:
#         return False
#     elif pos == len(list) - 1:
#         return True
#     elif list[pos] < list[pos + 1] and list[pos] < list[pos - 1]:
#         return True
#
#     return False

def cutMiddlePoints(v: []) -> []:
    v_len = len(v)
    i = 1
    while i < v_len - 1:
        if v[i] >= v[i + 1] and v[i] <= v[i - 1]:
            del v[i]
            v_len -= 1
            i -= 1

        elif v[i] <= v[i + 1] and v[i] >= v[i - 1]:
            del v[i]
            v_len -= 1
            i -= 1

        i +=1

    return v

def cutOtherPoints(v: []) -> []:
    if v[0] < v[1]:
        del v[0]
    if v[-1] > v[-2]:
        del v[-1]

    v_len = len(v)

    i = 0
    while i < v_len - 3:
        print("i:", i, file=sys.stderr)
        print("v_len:", v_len, file=sys.stderr)
        print("v:", v, file=sys.stderr)


        if v[i] >= v[i + 2] and v[i + 1] >= v[i + 3]:
            del v[i + 1]
            del v[i + 1]
            i -= 2
            v_len -= 2
            print("1", file=sys.stderr)


        elif v[i] <= v[i + 2] and v[i + 1] >= v[i + 3]:
            del v[i]
            del v[i]
            i -= 2
            v_len -= 2
            print("2", file=sys.stderr)

        elif v[i] >= v[i + 2] and v[i + 1] <= v[i + 3]:
            del v[i + 2]
            del v[i + 2]
            i -= 2
            v_len -= 2
            print("3", file=sys.stderr)

        i += 2
    return v

n = int(input())
v = []
for i in input().split():
    v.append(int(i))
print("v:       ", v, file=sys.stderr)

v = cutMiddlePoints(v)
print("v cut 0: ", v, file=sys.stderr)

if len(v) == 2:
    min = min(0, v[1] - v[0])
else:
    temp_v = []
    counter = 1
    while temp_v != v:
        temp_v = []
        print("v cut", counter, file=sys.stderr)
        temp_v.extend(v)
        cutOtherPoints(v)
        counter += 1

    min = 0
    for i in range(0, len(v), 2):
        temp = v[i + 1] - v[i]
        if temp < min:
            min = temp

print(min)