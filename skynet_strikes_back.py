import copy
import sys
import math
from collections import deque


class Node:
    def __init__(self, id: int):
        self.id = id
        self.linked_nodes = []
        self.gateway = False

    def children(self) -> []:
        return self.linked_nodes

    def dangerous_link(self):
        counter = 0
        for i in self.linked_nodes:
            if i.gateway:
                counter += 1
                if counter >= 2:
                    return i.id
        return None

    def add_child(self, node):
        id = node.id
        for i in self.linked_nodes:
            if i.id == id:
                return

        self.linked_nodes.append(node)


class Graph:
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

        node1.add_child(node2)
        node2.add_child(node1)

    def set_gateway(self, id: int):
        self.get_node(id).gateway = True

    def remove_link(self, n1: int, n2: int):
        node1 = self.get_node(n1)
        node2 = self.get_node(n2)
        node1.children().remove(node2)
        node2.children().remove(node1)

    def print_links(self):
        counter = 0
        for i in self.nodes:
            counter += len(i.children())

        print("n archi ", counter / 2, file=sys.stderr, flush=True)


def bfs(si: Node) -> Node:
    frontier = deque()
    frontier.append(si)
    explored = []
    while True:
        if len(frontier) < 1:
            return "fallimento"
        node = frontier.popleft()
        explored.append(node.id)

        for i in node.children():
            if (i.id not in explored) and (i not in frontier):
                if i.gateway:
                    return node
                frontier.append(i)


def predict_skynet_agent(si: Node, skynet_network: Graph) -> ():
    temp_graph = copy.deepcopy(skynet_network)
    temp_si = temp_graph.get_node(si.id)

    node_to_closest_gateway = bfs(temp_si)
    dangerous_gateway_id = node_to_closest_gateway.dangerous_link()

    step = 0
    print("step ", step, file=sys.stderr, flush=True)

    while dangerous_gateway_id is None:
        step += 1
        print("step ", step, file=sys.stderr, flush=True)

        for i in node_to_closest_gateway.children():
            if i.gateway:
                temp_graph.remove_link(i.id, node_to_closest_gateway.id)

        node_to_closest_gateway = bfs(node_to_closest_gateway)
        dangerous_gateway_id = node_to_closest_gateway.dangerous_link()

    print("fine ", file=sys.stderr, flush=True)

    skynet_network.remove_link(node_to_closest_gateway.id, dangerous_gateway_id)
    return node_to_closest_gateway.id, dangerous_gateway_id

n, l, e = [int(i) for i in input().split()]
print("l ", l, file=sys.stderr, flush=True)

skynet_network = Graph()

for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    skynet_network.add_node(n1)
    skynet_network.add_node(n2)
    skynet_network.add_link(n1, n2)


for i in range(e):
    ei = int(input())  # the index of a gateway node
    skynet_network.set_gateway(ei)

counter = 1
while True:
    print("MOSSA ", counter, file=sys.stderr)

    double_gateway = False
    for node in skynet_network.nodes:
        if node.dangerous_link() != None:
            double_gateway = True
            break

    print("double_gateway ", double_gateway, file=sys.stderr)

    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print("si: ", si, file=sys.stderr,flush=True)

    link_to_remove = None

    skynet_agent_node = skynet_network.get_node(si)

    for node in skynet_agent_node.children():
        if node.gateway:
            print("cancellazione obbligata", si, node.id, file=sys.stderr, flush=True)
            skynet_network.remove_link(si, node.id)
            link_to_remove = si, node.id
            break

    if link_to_remove is None:
        if double_gateway:
            print("cancellazione preventiva", file=sys.stderr, flush=True)
            link_to_remove = predict_skynet_agent(skynet_agent_node, skynet_network)
        else:
            print("niente di meglio da fare", file=sys.stderr, flush=True)
            for node in skynet_network.nodes:
                if node.gateway and len(node.children()) > 0:
                    link_to_remove = node.id, node.children()[0].id
                    skynet_network.remove_link(node.id, node.children()[0].id)
                    break

    print(link_to_remove[0], link_to_remove[1])

    counter += 1