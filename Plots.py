from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random

class GraphCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        fig.set_facecolor("none")
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = self.figure.add_subplot(111)
        fig.tight_layout()
        self.G = nx.Graph()
        self.ax.patch.set_alpha(0)
        self.pos = nx.random_layout(self.G)

    def set_nodes(self, nodes=[]):
        self.G.add_path(nodes)
        self.pos = {1: (4,4), 2: (1,1), 3: (8,9), 4: (2,10), 5: (4,10), 6: (6,9), 7: (5,6), 8: (1,8), 9: (8,7), 10: (9,4)}
        # self.pos = {}
        # n = len(self.G.nodes())
        # x_coords = random.sample(range(1, 1+n), n)
        # y_coords = random.sample(range(1, 1+n), n)
        # for i, node in enumerate(self.G.nodes()):
        #     self.pos.update({node: (x_coords[i], y_coords[i])})

    def get_nodes(self):
        return self.G.nodes()

    def plot(self, edges=[]):
        self.ax.clear()

        # pos = {'A': (1, 1), 'B': (2, 2), 'C': (3, 5), 'D': (4, 4), 'E': (5, 6), 'F': (6, 3), 'G': (7, 7), 'H': (8, 8)}
        # pos = nx.spring_layout(self.G)
        # pos = nx.spectral_layout(self.G)
        # pos = nx.shell_layout(self.G)
        # pos = nx.random_layout(self.G)

        nx.draw_networkx_nodes(self.G, self.pos, cmap=plt.get_cmap('jet'), node_size=500, ax=self.ax)
        nx.draw_networkx_labels(self.G, self.pos, ax=self.ax)
        nx.draw_networkx_edges(self.G, self.pos, cmap=plt.get_cmap('jet'), edgelist=edges, edge_color='b', arrows=False, ax=self.ax)
        self.draw()


class HistoryCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        fig.set_facecolor("none")
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = self.figure.add_subplot(111)
        fig.tight_layout()
        self.ax.patch.set_alpha(0)
