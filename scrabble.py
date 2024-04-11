import copy
import sys
import math

dictionary = set()
n = int(input())
for i in range(n):
    w = str(input())
    dictionary.add(w)
letters = []
letters.extend(str(input()))

letter_value = []
letter_value.append(["e", "a", "i", "o", "n", "r", "t", "l", "s", "u"])
letter_value.append(["d", "g"])
letter_value.append(["b", "c", "m", "p"])
letter_value.append(["f", "h", "v", "w", "y"])
letter_value.append(["k"])
letter_value.append(["j", "x"])
letter_value.append(["q", "z"])

points = {}
for i in range(len(letter_value)):
    for j in range(len(letter_value[i])):
        points[letter_value[i][j]] = i + 1

def value(current_word: str) -> int:
    value = 0
    for c in current_word:
        value += points[c]
    return value

def search_best_word(remaining_letters: [], current_word = "", max_word = "", max_value = 0) -> ():
    if current_word != "":
        if current_word in dictionary:
            temp_value = value(current_word)
            if temp_value > max_value:
                max_word = current_word
                max_value = temp_value
            # elif temp_value == max_value:
            #     if dictionary.index(current_word) < dictionary.index(max_word):
            #         max_word = current_word

    if len(remaining_letters) == 0:
        return max_word, max_value

    used_letters = []
    for i in range(len(remaining_letters)):
        temp_letters = copy.deepcopy(remaining_letters)
        c = temp_letters.pop(i)

        if c not in used_letters:

            temp_word, temp_value = search_best_word(temp_letters, current_word + c, max_word, max_value)
            used_letters.append(c)

            if temp_word != "":
                if temp_value > max_value:
                    max_word = temp_word
                    max_value = temp_value
                # elif temp_value == max_value:
                #     if dictionary.index(temp_word) < dictionary.index(max_word):
                #         max_word = temp_word

    return max_word, max_value

top_word, top_value = search_best_word(letters)

print(top_word)
