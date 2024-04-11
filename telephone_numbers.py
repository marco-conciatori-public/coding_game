import sys
import math

class Node:
    def __init__(self, id = None):
        self.id = id
        self.father = Node
        self.children = []

    def add_child(self, id: int):
        node = Node(id)
        for i in self.children:
            if i.id == id:
                return

        node.father = self
        self.children.append(node)

    def get_child(self, id: int):
        for i in self.children:
            if i.id == id:
                return i


class Tree:
    def __init__(self):
        self.root = Node()

    def add_number(self, number: []):
        node = self.root
        print("number ", number, file=sys.stderr)
        for i in number:
            print("i ", i, file=sys.stderr)

            node.add_child(i)
            node = node.get_child(i)

    def count_elements(self) -> int:
        count = -1
        frontier = []
        frontier.append(self.root)

        while len(frontier) > 0:
            count += 1
            node = frontier.pop(0)
            frontier.extend(node.children)

        return count


n = int(input())
numbers = []
tree = Tree()
for i in range(n):
    telephone = input()
    numbers = []
    for k in range(len(telephone)):
        numbers.append(int(telephone[k]))
    tree.add_number(numbers)

memory_usage = tree.count_elements()

print(memory_usage)