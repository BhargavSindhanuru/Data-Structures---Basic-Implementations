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

    def listOfNodeValues(self):
        return [i.value for i in self.nodes]


    def insertEdge(self, newedgeValue, nodeFromValue, nodeToValue):
        for node in self.nodes:
            if nodeFromValue == node.value:
                nodeFrom = node
            if nodeToValue == node.value:
                nodeTo = node
            newEdge = Edge(newedgeValue, nodeFrom, nodeTo)
            self.edges.append(newEdge)
            nodeFrom.edges.append(newEdge)
            nodeTo.edges.append(newEdge)
