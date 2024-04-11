import sys

class Node:
    def __init__(self, id: int):
        self.id = id
        self.linked_nodes = []

    def children(self) -> []:
        return self.linked_nodes

    def add_child(self, node):
        id = node.id
        for i in self.linked_nodes:
            if i.id == id:
                return

        self.linked_nodes.append(node)


class Graph:
    def __init__(self):
        self.nodes = []

    def __iter__(self):
        return self.nodes.__iter__()

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

        node1.add_child(node2)
        node2.add_child(node1)

    def remove_link(self, node1: Node, node2: Node):
        node2.children().remove(node1)
        node1.children().remove(node2)

# def number_of_moves(network: Graph) -> int:
#     counter = 0
#     while True:
#         if len(network.nodes) <= 3:
#             if len(network.nodes) == 1:
#                 return counter
#             return counter + 1
#         else:
#             nodes_to_remove = []
#             for node in network:
#                 if len(node.children()) == 1:
#                     nodes_to_remove.append(node)
#
#             for node in nodes_to_remove:
#                 network.remove_link(node, node.children()[0])
#                 network.nodes.remove(node)
#         counter += 1

def number_of_moves(network: Graph) -> int:
    counter = 0
    nodes_to_check = []
    for node in network:
        if len(node.children()) == 1:
            nodes_to_check.append(node)

    while True:
        if len(network.nodes) <= 3:
            if len(network.nodes) == 1:
                return counter
            return counter + 1
        else:
            nodes_to_remove = []
            for node in nodes_to_check:
                if len(node.children()) == 1 and node not in nodes_to_remove:
                    nodes_to_remove.append(node)

            nodes_to_check = []
            for node in nodes_to_remove:
                nodes_to_check.append(node.children()[0])
                network.remove_link(node, node.children()[0])
                network.nodes.remove(node)
        counter += 1

network = Graph()

n = int(input())
for i in range(n):
    xi, yi = [int(j) for j in input().split()]
    network.add_node(xi)
    network.add_node(yi)
    network.add_link(xi, yi)

moves = number_of_moves(network)

print(moves)
