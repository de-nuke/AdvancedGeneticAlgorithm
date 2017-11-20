from PyQt5 import QtCore
from window import Ui_MainWindow
# from w2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QVBoxLayout
import sys
from Plots import GraphCanvas, HistoryCanvas
from ApplicationLogic import ApplicationLogic


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.app = ApplicationLogic(self)

        self.left_plot_layout = QVBoxLayout(self.left_frame)
        self.graph_max_canvas = GraphCanvas()
        self.left_plot_layout.addWidget(self.graph_max_canvas)

        self.right_plot_layout = QVBoxLayout(self.right_frame)
        self.graph_min_canvas = GraphCanvas()
        self.right_plot_layout.addWidget(self.graph_min_canvas)

        self.top_plot_layout = QVBoxLayout(self.top_frame)
        self.history_canvas = HistoryCanvas()
        self.top_plot_layout.addWidget(self.history_canvas)

        self.apply_btn.clicked.connect(self.app.apply_click)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()

    sys.exit(app.exec_())