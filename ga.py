from PyQt5 import QtCore
from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QVBoxLayout
import sys
from Plots import GraphCanvas, HistoryCanvas


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.left_plot_layout = QVBoxLayout(self.left_frame)
        self.graph_canvas = GraphCanvas()
        self.left_plot_layout.addWidget(self.graph_canvas)

        self.right_plot_layout = QVBoxLayout(self.right_frame)
        self.history_canvas = HistoryCanvas()
        self.right_plot_layout.addWidget(self.history_canvas)

        self.graph_canvas.set_nodes([i for i in range(1,11)])

        self.graph_canvas.plot()
        self.pushButton.clicked.connect(self.graph_canvas.plot)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()

    sys.exit(app.exec_())