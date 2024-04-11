import sys
import math
from cmath import rect

gravity_acc = 3.711

my_x = float
my_y = float
my_h_speed = float
my_v_speed = float
my_rotate = int
my_fuel = int
my_power = int
direction = str

def find_next_peak(my_x: float, my_y: float, land_x: [int], land_y: [int], direction: str, landing_surface: dict) -> int:
    m = []
    m_max = float
    next_peak_position = int

    if direction == 'right':
        for i in range(len(land_x)):
            if land_x[i] > my_x and land_x[i] < landing_surface['x1']:
                m_temp = (land_y[i] - my_y) / (land_x[i] - my_x)
                if m_temp >= m_max:
                    m_max = m_temp
                    next_peak_position = i

    elif direction == 'left':
        for i in range(len(land_x)):
            if land_x[i] < my_x and land_x[i] > landing_surface['x2']:
                m_temp = (my_y - land_y[i]) / (my_x - land_x[i])
                if m_temp < m_min:
                    m_min = m_temp
                    next_peak_position = i

    return next_peak_position

def examine_surface(my_x: float, my_y: float, land_x: [int], land_y: [int]) -> ():
    landing_surface = dict

    for i in range(len(land_x) - 1):
        if land_y[i] == land_y[i + 1]:
            landing_surface = {'x1': land_x[i], 'x2': land_x[i + 1], 'y1': land_y[i], 'y2': land_x[i + 1]}

    if my_x < landing_surface['x1']:
        direction = 'right'
    elif my_x > landing_surface['x2']:
        direction = 'left'
    else:
        direction = 'down'

    return landing_surface, direction

def find_plan(my_x: float, my_y: float, my_h_speed: float, my_v_speed: float, my_rotate: int, my_fuel: int, my_power: int, plan_stage: int, land_x: [int], land_y: [int]) -> ():
    plan = ()

    if plan_stage == 1:
        pass

    return plan

def find_stage(my_x: float, my_h_speed: float, my_rotate: int, landing_surface: dict) -> int:
    if my_x < landing_surface['x1'] or my_x > landing_surface['x2']:
        plan_stage = 1
    elif my_rotate != 0 or abs(my_h_speed) > 20:
        plan_stage = 2
    else:
        plan_stage = 3

    return plan_stage

first_turn = True
plan_stage = 0

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    plan = ()

    if first_turn:
        first_turn = False
        my_x = x
        my_y = y
        my_h_speed = h_speed
        my_v_speed = v_speed
        my_rotate = rotate
        my_fuel = fuel
        my_power = power
        landing_surface, direction = examine_surface(my_x, my_y, land_x, land_y)

    new_plan_stage = find_stage(my_x, my_h_speed, my_rotate, landing_surface)

    if new_plan_stage != plan_stage:
        plan_stage = new_plan_stage
        plan = find_plan(my_x, my_y, my_h_speed, my_v_speed, my_rotate, my_fuel, my_power, plan_stage, land_x, land_y)

    new_rotate = -45
    if new_rotate >= -90 and new_rotate <= 90:
        if new_rotate > (my_rotate + 15):
            my_rotate += 15
        elif new_rotate < (my_rotate - 15):
            my_rotate -= 15
        else:
            my_rotate = new_rotate

    new_power = 4
    if new_power >= 0 and new_power <= 4:
        if new_power < my_power:
            my_power -= 1
        elif new_power > my_power:
            my_power += 1

    h_accel = my_power * math.sin(math.radians(-my_rotate))
    v_accel = my_power * math.cos(math.radians(my_rotate)) - gravity_acc

    my_x = my_x + my_h_speed + h_accel / 2.0
    my_y = my_y + my_v_speed + v_accel / 2.0

    my_h_speed += h_accel
    my_v_speed += v_accel
    my_fuel -= my_power

    print("v_speed_int: " + str(round(my_v_speed)), file=sys.stderr)
    print("h_speed_int: " + str(round(my_h_speed)), file=sys.stderr)
    print("my_y_int: " + str(round(my_y)), file=sys.stderr)
    print("my_x_int: " + str(round(my_x)), file=sys.stderr)
    # print("fuel: " + str(my_fuel), file=sys.stderr)
    print("my_rotate: " + str(my_rotate), file=sys.stderr)
    # print("new_power: " + str(neW_power), file=sys.stderr)

    print(plan)
