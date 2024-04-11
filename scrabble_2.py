import copy
import sys
import math


class Node:
    def __init__(self, letter = None, father = None):
        self.letter = letter
        self.father = father
        self.children = []
        self.is_word = False
        self.position = 0
        self.value = 0

    def add_child(self, letter: chr):
        for i in self.children:
            if i.letter == letter:
                return

        node = Node(letter, self)
        node.value = self.value + points[letter]
        self.children.append(node)

    def get_child(self, letter: chr):
        for i in self.children:
            if i.letter == letter:
                return i


class Tree:
    def __init__(self):
        self.root = Node()

    def add_word(self, word: str, position: int):
        node = self.root
        print("word ", word, file=sys.stderr)
        for letter in word:
            print("letter", letter, file=sys.stderr)

            node.add_child(letter)
            node = node.get_child(letter)

        node.is_word = True
        node.position = position

def dfs(remaining_letters: [], current_node: Node, max_node: Node) -> Node:
    if current_node.is_word:
        if current_node.value > max_node.value:
            max_node = current_node
        elif current_node.value == max_node.value:
            if current_node.position < max_node.position:
                max_node = current_node

    if len(remaining_letters) == 0:
        return max_node

    for i in range(len(remaining_letters)):
        temp_letters = copy.deepcopy(remaining_letters)
        letter = temp_letters.pop(i)
        child = current_node.get_child(letter)
        if child is not None:
            temp_node = dfs(temp_letters, child, max_node)
            if temp_node.value > max_node.value:
                max_node = temp_node
            elif temp_node.value == max_node.value:
                if temp_node.position < max_node.position:
                    max_node = temp_node
    return max_node

dictionary_tree = Tree()

n = int(input())
words = []
for i in range(n):
    words.append(str(input()))

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
print("1", flush=True, file=sys.stderr)

values = [1, 2, 3, 4, 5, 8, 10]

points = {}
for i in range(len(letter_value)):
    for j in range(len(letter_value[i])):
        points[letter_value[i][j]] = values[i]

print("2", flush=True, file=sys.stderr)

for i in range(len(words)):
    dictionary_tree.add_word(words[i], i)
print("3", flush=True, file=sys.stderr)

top_node = dfs(letters, dictionary_tree.root, Node())
print("4", flush=True, file=sys.stderr)

node = top_node
top_word = ""
while node.father is not None:
    top_word = node.letter + top_word

print(top_word)
