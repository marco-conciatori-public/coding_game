import sys
import math

r = int(input())
l = int(input())

sequence = []
sequence.append(r)

for i in range(l - 1):
    new_sequence = []

    while len(sequence) > 0:
        first = sequence.pop(0)
        counter = 1

        while len(sequence) > 0:
            if first == sequence[0]:
                del sequence[0]
                counter += 1
            else:
                break
        new_sequence.append(counter)
        new_sequence.append(first)
    sequence = new_sequence

for k in range(len(sequence)):
    print(sequence[k], end = "")
    if k < len(sequence) - 1:
        print(end=" ")

print("len(sequence):", len(sequence), file=sys.stderr)
