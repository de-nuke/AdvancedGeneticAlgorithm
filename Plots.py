from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import networkx as nx
from settings import *
import numpy


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
        pos = dict()
        for node in nodes:
            pos.update({node: POSITIONS[node]})
        self.pos = pos

    def get_nodes(self):
        return self.G.nodes()

    def plot(self, edges=[]):
        self.ax.clear()
        self.G.add_edges_from(edges)

        nx.draw_networkx_nodes(self.G, self.pos, cmap=plt.get_cmap('jet'), node_size=400, ax=self.ax)
        nx.draw_networkx_labels(self.G, self.pos, ax=self.ax)
        nx.draw_networkx_edges(self.G, self.pos, cmap=plt.get_cmap('jet'), edgelist=edges, edge_color='b', arrows=False, ax=self.ax)
        self.ax.patch.set_alpha(0)
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
        # fig.tight_layout()
        self.txt = self.ax.text(0.5, 0.9, '', transform=self.ax.transAxes, bbox=dict(facecolor='green', alpha=0.5), horizontalalignment='center')
        self.ax.patch.set_alpha(0)
        self.y_lim = ()

    def plot(self, max_hist, avg_hist, min_hist):
        # self.ax.cla()
        try:
            x = range(len(max_hist))
            self.ax.lines[0].set_data(x, max_hist)
            self.ax.lines[1].set_data(x, avg_hist)
            self.ax.lines[2].set_data(x, min_hist)
        except IndexError:
            print('był index error')
            self.ax.plot(max_hist)  # Lots of overhead. Do once.
            self.ax.plot(avg_hist)  # Lots of overhead. Do once.
            self.ax.plot(min_hist)  # Lots of overhead. Do once.

        # self.y_lim = self.ax.get_ylim()
        if min_hist and max_hist:
            self.ax.set_ylim([0.9 * min(min_hist), 1.1 * max(max_hist)])
            self.txt.set_text('Maximum = {}, Minimum = {}, Average = {}'.format(round(max_hist[-1], 2), round(min_hist[-1], 2), round(avg_hist[-1], 2)))
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        self.draw()
        # self.ax.plot(max_history, style + 'go', linewidth=6, markeredgecolor='yellow', markeredgewidth=1)
        # self.ax.plot(avg_history, style + 'co', linewidth=3, markeredgecolor='black', markeredgewidth=1)
        # self.ax.plot(min_history, style + 'ro', linewidth=0.8, markeredgecolor='black', markeredgewidth=1)
