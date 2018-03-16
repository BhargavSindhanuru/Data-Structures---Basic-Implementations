class Node():
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge():
    def __init__(self, value, nodeFrom, nodeTo):
        self.value = value
        self.nodeFrom = nodeFrom
        self.nodeTo = nodeTo

class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insertNode(self, newNodeValue):
        newNode = Node(newNodeValue)
        self.nodes.append(newNode)

