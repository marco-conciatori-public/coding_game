import sys

temp = []
l, h = [int(i) for i in input().split()]

for i in range(h):
    numeral = input()
    temp.append(numeral)

mayan_digits = []
for i in range(20):
    digit = []
    for row in temp:
        digit.append(row[(i * l):((i + 1) * l)])
    mayan_digits.append(digit)

num_1 = []
s1 = int(input())
digit_number = int(s1 / h)

for i in range(digit_number):
    digit = []

    for j in range(h):
        num_1line = input()
        digit.append(num_1line)
    num_1.append(digit)

num_2 = []
s2 = int(input())
digit_number = int(s2 / h)
for i in range(digit_number):
    digit = []

    for j in range(h):
        num_2line = input()
        digit.append(num_2line)
    num_2.append(digit)

operator = input()


def mayan_to_decimal(mayan_number: []) -> int:
    decimal_number = 0
    counter = 0
    for digit in reversed(mayan_number):
        n = mayan_digits.index(digit)
        decimal_number += 20 ** counter * n
        counter += 1
    return decimal_number


def decimal_to_mayan(decimal_number: int) -> []:
    mayan_number = []
    reminder = decimal_number
    if decimal_number != 0:
        while reminder > 0:
            reminder, digit = divmod(reminder, 20)
            print("reminder", reminder, flush=True, file=sys.stderr)
            print("digit", digit, flush=True, file=sys.stderr)
            mayan_digit = mayan_digits[digit]
            mayan_number.insert(0, mayan_digit)
    else:
        mayan_number = [mayan_digits[0]]

    return mayan_number

decimal_n1 = mayan_to_decimal(num_1)
print("decimal_n1", decimal_n1, file=sys.stderr)

decimal_n2 = mayan_to_decimal(num_2)
print("decimal_n2", decimal_n2, file=sys.stderr)
print("operator", operator, flush=True, file=sys.stderr)

decimal_result = 0
if operator == "+":
    decimal_result = decimal_n1 + decimal_n2
elif operator == "-":
    decimal_result = decimal_n1 - decimal_n2
elif operator == "*":
    decimal_result = decimal_n1 * decimal_n2
elif operator == "/":
    decimal_result = int(decimal_n1 / decimal_n2)
else:
    print("problema", file=sys.stderr)

print("decimal_result", decimal_result, file=sys.stderr)
mayan_result = decimal_to_mayan(decimal_result)

for mayan_digit in mayan_result:
    for row in mayan_digit:
        print(row)
