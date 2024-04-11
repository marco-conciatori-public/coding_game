import sys
from collections import deque


class Node:
    def __init__(self, id = None):
        self.id = id
        self.children = []
        self.depth = 0
        self.is_root = True

    def get_child(self, id: int):
        for i in self.children:
            if i.id == id:
                return i


class Tree:
    def __init__(self):
        self.nodes = []

    def __contains__(self, id: int):
        for i in self.nodes:
            if i.id == id:
                return True
        return False

    def get_node(self, id: int) -> Node:
        for i in self.nodes:
            if i.id == id:
                return i

    def add_node(self, n1: int):
        if n1 not in self:
            node1 = Node(n1)
            self.nodes.append(node1)

    def add_link(self, n1: int, n2: int):
        node1 = self.get_node(n1)
        node2 = self.get_node(n2)

        node2.is_root = False

        node1.children.append(node2)

    def max_height(self, node) -> int:
        depth = 1
        node.depth = depth

        frontier = deque()
        frontier.append(node)

        while len(frontier) > 0:
            node = frontier.popleft()

            depth = max(depth, node.depth)

            for i in node.children:
                i.depth = max(i.depth, node.depth + 1)
                if i not in frontier:
                    frontier.append(i)

        return depth

    def reset_depths(self):
        for i in self.nodes:
            i.depth = 0


n = int(input())  # the number of relationships of influence
tree = Tree()

for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    tree.add_node(x)
    tree.add_node(y)
    tree.add_link(x, y)
    print("x, y", x, y, file=sys.stderr)
    print("tree.add_nodes(x, y)", tree.get_node(x).id, tree.get_node(y).id,  file=sys.stderr)

chain_lenght = 0
for node in tree.nodes:
    if node.is_root:
        tree.reset_depths()
        chain_lenght = max(chain_lenght, tree.max_height(node))

# The number of people involved in the longest succession of influences
print(chain_lenght)
