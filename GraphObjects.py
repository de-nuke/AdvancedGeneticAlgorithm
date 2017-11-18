from math import sqrt


class Node:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def pos(self):
        return self.x, self.y

    def __repr__(self):
        return '{}({},{})'.format(self.label, self.x, self.y)


class Edge:
    def __init__(self, node1, node2):
        self.nodes = (node1.label, node2.label)
        self.length = sqrt((node1.x - node2.x) ** 2 + (node2.x - node2.y) ** 2)
        self.pos = (node1.x, node1.y, node2.x, node2.y)

    def __str__(self):
        return "{}-{}".format(*self.nodes)


class Path:
    """
    Path is a list of edges and nodes
    """

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        for i in range(len(nodes) - 1):
            self.edges.append(Edge(nodes[i], nodes[i + 1]))
        self.length = sum([edge.length for edge in self.edges])

    @property
    def id(self):
        str_self = str(self)
        return str_self.replace('-', '') if '-' in str_self else str_self

    def __str__(self):
        string = ''
        for i, edge in enumerate(self.edges):
            if i == 0:
                string += str(edge)
            else:
                string += str(edge)[1:]
        return string

    def __repr__(self):
        return str(self) + ' LEN=' + str(round(self.length, 2))
