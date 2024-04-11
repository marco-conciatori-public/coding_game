import sys
import math

def next_room(xi: int, yi: int, pos: str, grid: []):
    type = grid[yi][xi]
    x = xi
    y = yi

    if pos == "TOP":
        if type == 1 or type == 3 or type == 7 or type == 9:
            x += 1
        elif type == 4 or type == 10:
            y -= 1
        elif type == 5 or type == 11:
            y += 1
        else:
            print("BOOOOOOOM!!!! (TOP)", file=sys.stderr)

    elif pos == "LEFT":
        if type == 1 or type == 5 or type == 8 or type == 9 or type == 13:
            x += 1
        elif type == 2 or type == 6:
            y += 1
        else:
            print("BOOOOOOOM!!!! (LEFT)", file=sys.stderr)
    elif pos == "RIGHT":
        if type == 1 or type == 4 or type == 7 or type == 8 or type == 12:
            x += 1
        elif type == 2 or type == 6:
            y -= 1
        else:
            print("BOOOOOOOM!!!! (RIGHT)", file=sys.stderr)
    else:
        print("cose strane", file=sys.stderr)

    return x, y

w, h = [int(i) for i in input().split()]
print("w:", w, file=sys.stderr)
print("h:", h, file=sys.stderr)

grid = []

for i in range(h):
    line = [int(j) for j in input().split()]
    grid.append(line)

ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    x, y = next_room(xi, yi, pos, grid)

    print(x, y)
