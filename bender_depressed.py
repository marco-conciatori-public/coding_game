import copy
import sys
import math

l, c = [int(i) for i in input().split()]
directions = {"S": "SOUTH", "E": "EAST", "N": "NORTH", "W": "WEST"}


class City:
    def __init__(self, grid: []):
        self.grid = [list(x) for x in zip(*grid)]
        self.destroyed_obstacles = 0

    def get_cell(self, x: int, y: int) -> chr:
        return self.grid[x][y]

    def set_cell(self, x: int, y: int, c: chr) -> chr:
        self.grid[x][y] = c

    def get_pos(self, c: chr) -> []:
        grid = self.grid
        pos = []

        for y in range(len(grid[0])):
            for x in range(len(grid)):
                if grid[x][y] == c:
                    pos.append([x, y])
        return pos


class Bender:
    def __init__(self, city: City):
        self.city = city
        self.position = city.get_pos("@")[0]
        self.breaker = False
        self.direction = "SOUTH"
        self.loop = False
        self.inverse = False
        self.past_states = []
        self.city.set_cell(self.position[0], self.position[1], " ")

    def examine_current_cell(self) -> str:
        current_cell = self.city.get_cell(self.position[0], self.position[1])
        state = [self.position, self.direction]
        #print("state", state, file=sys.stderr)
        #print("past_states", self.past_states, file=sys.stderr)
        state = (self.position, self.direction, self.inverse, self.breaker, self.city.destroyed_obstacles)
        if state in self.past_states:
            self.loop = True
            return "end"
        else:
            self.past_states.append(copy.deepcopy(state))
            if current_cell in directions:
                self.direction = directions[current_cell]
            elif current_cell == "$":
                return "end"
            elif current_cell == "B":
                self.breaker = not self.breaker
            elif current_cell == "I":
                self.inverse = not self.inverse
            elif current_cell == "T":
                teleports = self.city.get_pos("T")
                t1 = teleports[0]
                t2 = teleports[1]
                if self.position == t1:
                    self.position = t2
                else:
                    self.position = t1
        return "continue"

    def step(self, counter = 0) -> str:
        next_position = self.next_position()
        print("position", self.position, file=sys.stderr)
        print("next_position", next_position, file=sys.stderr)
        print("direction", self.direction, file=sys.stderr)
        next_cell = self.city.get_cell(next_position[0], next_position[1])
        print("next_cell", next_cell, file=sys.stderr)
        if next_cell == "#" or (next_cell == "X" and not self.breaker):
            print("caso 1", file=sys.stderr)

            if not self.inverse:
                if counter == 0:
                    self.direction = "SOUTH"
                elif counter == 1:
                    self.direction = "EAST"
                elif counter == 2:
                    self.direction = "NORTH"
                elif counter == 3:
                    self.direction = "WEST"
            else:
                if counter == 3:
                    self.direction = "SOUTH"
                elif counter == 2:
                    self.direction = "EAST"
                elif counter == 1:
                    self.direction = "NORTH"
                elif counter == 0:
                    self.direction = "WEST"
            return self.step(counter + 1)
        elif next_cell == "X" and self.breaker:
            print("caso 2", file=sys.stderr)

            self.city.set_cell(next_position[0], next_position[1], " ")
            self.city.destroyed_obstacles += 1
            self.position = next_position
            return self.direction
        else:
            print("caso 3", file=sys.stderr)

            self.position = next_position
            return self.direction

    def next_position(self) -> ():
        pos = copy.deepcopy(self.position)
        if self.direction == "SOUTH":
            pos[1] += 1
        elif self.direction == "EAST":
            pos[0] += 1
        elif self.direction == "NORTH":
            pos[1] -= 1
        elif self.direction == "WEST":
            pos[0] -= 1

        return pos

    def print_city(self):
        grid = self.city.grid
        pos_x = self.position[0]
        pos_y = self.position[1]

        for y in range(len(grid[0])):
            for x in range(len(grid)):
                if pos_x == x and pos_y == y:
                    print("@", sep="", end="", file=sys.stderr)
                else:
                    print(grid[x][y], sep="", end="", file=sys.stderr)
            print(file=sys.stderr)


grid = []
for i in range(l):
    row = input()
    grid_row = []
    grid_row.extend(row)
    print("row", row, file=sys.stderr)

    grid.append(grid_row)

city = City(grid)

bender = Bender(city)

answer = []
control = "continue"
while True:
    bender.print_city()
    control = bender.examine_current_cell()
    if control == "end":
        break
    answer.append(bender.step())

if bender.loop:
    answer = ["LOOP"]

for s in answer:
    print(s)
