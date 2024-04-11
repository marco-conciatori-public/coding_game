import copy
import sys
import math

m = int(input())  # the amount of motorbikes to control
v = int(input())  # the minimum amount of motorbikes that must survive
l0 = input()  # L0 to L3 are lanes of the road. A dot character . represents a safe space, a zero 0 represents a hole in the road.
l1 = input()
l2 = input()
l3 = input()

road = []
road.append(l0)
road.append(l1)
road.append(l2)
road.append(l3)

road_lenght = len(road[0])
max_index = len(road[0]) - 1

def up1(x: int, y: [], s: int) ->():
    survivors = 0
    temp_y = copy.deepcopy(y)

    if s == 0:
        return False, 0
    if temp_y[0]:
        return False, 0
    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike - 1][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            if "0" not in road[motorbike][x + 1:min(max_index, x + s)] and "0" not in road[motorbike - 1][x + 1:min(max_index, x + s + 1)]:
                survivors += 1
            else:
                temp_y[motorbike] = False
    if survivors >= m:
        for i in range(3):
            if temp_y[i + 1]:
                temp_y[i] = True
            else:
                temp_y[i] = False
        temp_y[3] = False
        return True, temp_y
    return False, 0


def down1(x: int, y: [], s: int) ->():
    survivors = 0
    temp_y = copy.deepcopy(y)
    if s == 0:
        return False, 0
    if temp_y[3]:
        return False, 0
    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            print("road[motorbike]:", road[motorbike + 1][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            if "0" not in road[motorbike][x + 1:min(max_index, x + s)] and "0" not in road[motorbike + 1][x + 1:min(max_index, x + s + 1)]:
                survivors += 1
            else:
                temp_y[motorbike] = False
    if survivors >= m:
        for i in range(3, 0, -1):
            if temp_y[i - 1]:
                temp_y[i] = True
            else:
                temp_y[i] = False
        temp_y[0] = False
        return True, temp_y
    return False, 0


def speed1(x: int, y: [], s: int) ->():
    survivors = 0
    if s >= 50:
        return False, 0
    temp_y = copy.deepcopy(y)

    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s + 2)], file=sys.stderr)
            if "0" not in road[motorbike][x + 1:min(max_index, x + s + 2)]:
                survivors += 1
            else:
                temp_y [motorbike] = False
    if survivors >= m:
        return True, temp_y 
    return False, 0


def slow1(x: int, y: [], s: int) ->():
    survivors = 0
    temp_y = copy.deepcopy(y)
    if s <= 1:
        return False, 0
    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s)], file=sys.stderr)
            if "0" not in road[motorbike][x + 1:min(max_index, x + s)]:
                survivors += 1
            else:
                temp_y [motorbike] = False
    if survivors >= m:
        return True, temp_y
    return False, 0


def jump1(x: int, y: [], s: int) ->():
    survivors = 0
    temp_y = copy.deepcopy(y)
    if s == 0:
        return False, 0

    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            if road_lenght <= x + s + 1:
                print("fine strada", file=sys.stderr)
                return True, temp_y

            print("landing point:", road[motorbike][x + s], file=sys.stderr)
            if "0" != road[motorbike][x + s]:
                survivors += 1
            else:
                temp_y [motorbike] = False
    if survivors >= m:
        return True, temp_y
    return False, 0


def dfs1(x: int, y: [], s: int, counter = 0) ->():
    if x >= 500:
        return True, []

    if counter >= 50:
        return False, []
    print(file=sys.stderr)

    print("s:", s, file=sys.stderr)
    for i in range(len(road)):
        for k in range(len(road[i])):
            if k == x and y[i]:
                print("M", end="", file=sys.stderr)
            else:
                print(road[i][k], end="", file=sys.stderr)
        print(file=sys.stderr)

    print("if speed", file=sys.stderr)
    valid_move, new_y = speed1(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)

    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs1(x + s + 1, new_y, s + 1, counter + 1)
        if valid_solution:
            solution.insert(0, "SPEED")
            return True, solution

    print("if up", file=sys.stderr)
    valid_move, new_y = up1(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)
    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs1(x + s, new_y, s, counter + 1)
        if valid_solution:
            solution.insert(0, "UP")
            return True, solution

    print("if down", file=sys.stderr)
    valid_move, new_y = down1(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)
    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs1(x + s, new_y, s, counter + 1)
        if valid_solution:
            solution.insert(0, "DOWN")
            return True, solution

    print("if jump", file=sys.stderr)
    valid_move, new_y = jump1(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)
    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs1(x + s, new_y, s, counter + 1)
        if valid_solution:
            solution.insert(0, "JUMP")
            return True, solution

    print("if slow", file=sys.stderr)
    valid_move, new_y = slow1(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)
    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs1(x + s - 1, new_y, s - 1, counter + 1)
        if valid_solution:
            solution.insert(0, "SLOW")
            return True, solution

    return False, []


def up(x: int, y: [], s: int) ->():
    survivors = 0
    temp_y = copy.deepcopy(y)

    if s == 0:
        return False, 0
    if temp_y[0]:
        return False, 0
    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike - 1][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            if "0" not in road[motorbike][x + 1:min(max_index, x + s)] and "0" not in road[motorbike - 1][x + 1:min(max_index, x + s + 1)]:
                survivors += 1
            else:
                temp_y[motorbike] = False
    if survivors >= v:
        for i in range(3):
            if temp_y[i + 1]:
                temp_y[i] = True
            else:
                temp_y[i] = False
        temp_y[3] = False
        return True, temp_y
    return False, 0


def down(x: int, y: [], s: int) ->():
    survivors = 0
    temp_y = copy.deepcopy(y)
    if s == 0:
        return False, 0
    if temp_y[3]:
        return False, 0
    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            print("road[motorbike]:", road[motorbike + 1][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            if "0" not in road[motorbike][x + 1:min(max_index, x + s)] and "0" not in road[motorbike + 1][x + 1:min(max_index, x + s + 1)]:
                survivors += 1
            else:
                temp_y[motorbike] = False
    if survivors >= v:
        for i in range(3, 0, -1):
            if temp_y[i - 1]:
                temp_y[i] = True
            else:
                temp_y[i] = False
        temp_y[0] = False
        return True, temp_y
    return False, 0


def speed(x: int, y: [], s: int) ->():
    survivors = 0
    if s >= 50:
        return False, 0
    temp_y = copy.deepcopy(y)

    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s + 2)], file=sys.stderr)
            if "0" not in road[motorbike][x + 1:min(max_index, x + s + 2)]:
                survivors += 1
            else:
                temp_y [motorbike] = False
    if survivors >= v:
        return True, temp_y
    return False, 0


def slow(x: int, y: [], s: int) ->():
    survivors = 0
    temp_y = copy.deepcopy(y)
    if s <= 1:
        return False, 0
    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s)], file=sys.stderr)
            if "0" not in road[motorbike][x + 1:min(max_index, x + s)]:
                survivors += 1
            else:
                temp_y [motorbike] = False
    if survivors >= v:
        return True, temp_y
    return False, 0


def jump(x: int, y: [], s: int) ->():
    survivors = 0
    temp_y = copy.deepcopy(y)
    if s == 0:
        return False, 0

    for motorbike in range(len(temp_y)):
        if temp_y[motorbike]:
            print("motorbike:", motorbike, file=sys.stderr)
            print("road[motorbike]:", road[motorbike][x + 1:min(max_index, x + s + 1)], file=sys.stderr)
            if road_lenght <= x + s + 1:
                print("fine strada", file=sys.stderr)
                return True, temp_y

            print("landing point:", road[motorbike][x + s], file=sys.stderr)
            if "0" != road[motorbike][x + s]:
                survivors += 1
            else:
                temp_y [motorbike] = False
    if survivors >= v:
        return True, temp_y
    return False, 0


def dfs(x: int, y: [], s: int, counter = 0) ->():
    if x >= 500:
        return True, []

    if counter >= 50:
        return False, []
    print(file=sys.stderr)

    print("s:", s, file=sys.stderr)
    for i in range(len(road)):
        for k in range(len(road[i])):
            if k == x and y[i]:
                print("M", end="", file=sys.stderr)
            else:
                print(road[i][k], end="", file=sys.stderr)
        print(file=sys.stderr)

    print("if speed", file=sys.stderr)
    valid_move, new_y = speed(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)

    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs(x + s + 1, new_y, s + 1, counter + 1)
        if valid_solution:
            solution.insert(0, "SPEED")
            return True, solution

    print("if up", file=sys.stderr)
    valid_move, new_y = up(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)
    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs(x + s, new_y, s, counter + 1)
        if valid_solution:
            solution.insert(0, "UP")
            return True, solution

    print("if down", file=sys.stderr)
    valid_move, new_y = down(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)
    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs(x + s, new_y, s, counter + 1)
        if valid_solution:
            solution.insert(0, "DOWN")
            return True, solution

    print("if jump", file=sys.stderr)
    valid_move, new_y = jump(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)
    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs(x + s, new_y, s, counter + 1)
        if valid_solution:
            solution.insert(0, "JUMP")
            return True, solution

    print("if slow", file=sys.stderr)
    valid_move, new_y = slow(x, y, s)
    print("valid_move:", valid_move, file=sys.stderr)
    if valid_move:
        print("new_y:", new_y, file=sys.stderr)
        valid_solution, solution = dfs(x + s - 1, new_y, s - 1, counter + 1)
        if valid_solution:
            solution.insert(0, "SLOW")
            return True, solution

    return False, []

motorbikes_y = [False, False, False, False]
motorbikes_x = 0
counter = 0
while True:
    s = int(input())  # the motorbikes' speed
    for i in range(m):
        x, y, a = [int(j) for j in input().split()]
        motorbikes_x = x
        if a == 1:
            motorbikes_y[y] = True

    valid_solution, solution = dfs1(motorbikes_x, motorbikes_y, s, counter)
    if not valid_solution:
        valid_solution, solution = dfs(motorbikes_x, motorbikes_y, s, counter)

    counter += 1

    for move in solution:
        print(move)