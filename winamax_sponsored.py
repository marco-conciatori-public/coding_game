import sys
import math

def value(card: str):
    """ returns the int value of the card
    :rtype: int
    """
    value = card[:-1]

    if value == "J":
        return 11
    elif value == "Q":
        return 12
    elif value == "K":
        return 13
    elif value == "A":
        return 14

    return int(value)

def war(subdeck1, subdeck2, deck1: [], deck2: []):
    tempdeck1 = []
    if type(subdeck1) is list:
        tempdeck1.extend(subdeck1)
    else:
        tempdeck1.append(subdeck1)

    tempdeck2 = []
    if type(subdeck2) is list:
        tempdeck2.extend(subdeck2)
    else:
        tempdeck2.append(subdeck2)

    waroutput = ()

    if len(deck1) < 4 or len(deck2) < 4:
        waroutput = ("PAT", 0, 0)
        return waroutput

    tempdeck1.extend(deck1[x] for x in range(3))
    tempdeck2.extend(deck2[x] for x in range(3))

    deck1 = deck1[3:]
    deck2 = deck2[3:]

    tempdeck1.append(deck1[0])
    tempdeck2.append(deck2[0])

    deck1 = deck1[1:]
    deck2 = deck2[1:]

    if value(tempdeck1[-1]) > value(tempdeck2[-1]):
        deck1.extend(tempdeck1)
        deck1.extend(tempdeck2)
        waroutput = ("noPAT", deck1, deck2)
    elif value(tempdeck1[-1]) < value(tempdeck2[-1]):
        deck2.extend(tempdeck1)
        deck2.extend(tempdeck2)
        waroutput = ("noPAT", deck1, deck2)
    else:
        waroutput = war(tempdeck1, tempdeck2, deck1, deck2)

    return waroutput

n = int(input())  # the number of cards for player 1
deck1 = []
deck2 = []

for i in range(n):
    deck1.append(input())  # the n cards of player 1

m = int(input())  # the number of cards for player 2
for i in range(m):
    deck2.append(input())  # the m cards of player 2

if n == 0:
    output = "2 0"
    if m == 0:
        output = "PAT"
elif m == 0:
    output = "1 0"
else:
    round = 0
    while True:
        round += 1

        print("     ROUND " + str(round), file = sys.stderr)
        print("deck1:", end = " ", file=sys.stderr)
        for s in deck1:
            print(s, end = " ", file=sys.stderr)
        print(file=sys.stderr)
        print("deck2:", end = " ", file=sys.stderr)
        for s in deck2:
            print(s, end = " ", file=sys.stderr)
        print(file=sys.stderr)
        print(file=sys.stderr)

        card1 = deck1[0]
        card2 = deck2[0]

        deck1 = deck1[1:]
        deck2 = deck2[1:]

        waroutput = ()

        if value(card1) > value(card2):
            deck1.append(card1)
            deck1.append(card2)
        elif value(card1) < value(card2):
            deck2.append(card1)
            deck2.append(card2)
        else:
            waroutput = war(card1, card2, deck1, deck2)
            if waroutput[0] == "PAT":
                output = "PAT"
                break
            deck1 = waroutput[1]
            deck2 = waroutput[2]

        if len(deck1) == 0:
            output = "2 " + str(round)
            break
        if len(deck2) == 0:
            output = "1 " + str(round)
            break

        print("deck1:", end = " ", file=sys.stderr)
        for s in deck1:
            print(s, end = " ", file=sys.stderr)
        print(file=sys.stderr)
        print("deck2:", end = " ", file=sys.stderr)
        for s in deck2:
            print(s, end = " ", file=sys.stderr)
        print(file=sys.stderr)
        print(file=sys.stderr)

print(output)

#
# deck1 = ["6H", "7H", "6C", "QS", "7S", "8D", "6D", "5S", "6S", "QH", "4D", "3S", "7C", "3C", "4S", "5H", "QD", "5C", "3H", "3D", "8C", "4H", "4C", "QC", "5D", "7D"]
# deck2 = ["JH", "AH", "KD", "AD", "9C", "2D", "2H", "JC", "10C", "KC", "10D", "JS", "JD", "9D", "9S", "KS", "AS", "KH", "10S", "8S", "2S", "10H", "8H", "AC", "2C", "9H"]
#
# print("deck1:", end=" ", file=sys.stderr)
# for s in deck1:
#     print(s, end=" ", file=sys.stderr)
# print(file=sys.stderr)
# print("deck2:", end=" ", file=sys.stderr)
# for s in deck2:
#     print(s, end=" ", file=sys.stderr)
# print(file=sys.stderr)
# print(file=sys.stderr)
#
# output = gameround(deck1, deck2, 0)
# print(output)
