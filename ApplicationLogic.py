from Algorithm import Population
from PyQt5.QtCore import QThread, pyqtSignal
import random


class Plotter(QThread):

    def __init__(self, app):
        QThread.__init__(self)
        self.app = app
        self.main = app.main
        self.population = app.population
        self.isRunning = False
        self.mode = 'ENDLESS'

    def activate(self, mode):
        self.isRunning = True
        self.mode = mode

    def stop(self):
        self.isRunning = False

    def run(self):
        while True:
            if self.isRunning and self.app.current_iteration <= self.app.iterations_limit:
                self.main.progress_bar_text.setText('Iteration: {}/{}'.format(self.app.current_iteration, self.app.iterations_limit))
                self.population.reproduce().cross().mutate()
                self.app.current_iteration += 1

                self.app.max_hist.append(self.population.longest_path().length)
                self.app.avg_hist.append(self.population.average_path_length())
                self.app.min_hist.append(self.population.shortest_path().length)

                self.main.graph_max_canvas.plot(self.population.shortest_path().edges)
                self.main.graph_min_canvas.plot(self.population.longest_path().edges)
                self.main.history_canvas.plot(self.app.max_hist, self.app.avg_hist, self.app.min_hist)


class ApplicationLogic:
    def __init__(self, main_window):
        self.main = main_window
        self.population = Population()
        self.population.set_progress_bar(self.main.progressBar, self.main.progress_bar_text)
        self.max_hist = []
        self.min_hist = []
        self.avg_hist = []
        self.is_running = False
        self.thread = Plotter(self)
        self.iterations_limit = self.main.iterations.value()
        self.current_iteration = 1
        self.main.stop_btn.clicked.connect(self.thread.stop)

        self.main.graph_max_canvas.set_nodes(self.population.cities)
        self.main.graph_min_canvas.set_nodes(self.population.cities)

    def apply_click(self):
        self.main.apply_btn.setText('Applying...')
        self.main.progressBar.show()
        self.population.set_parameters(
            size=self.main.size.value(),
            iterations=self.main.iterations.value(),
            mutation_prob=self.main.mutation_prob.value()
        )

        self.iterations_limit = self.main.iterations.value()

        self.main.graph_max_canvas.plot(self.population.shortest_path().edges)
        self.main.graph_min_canvas.plot(self.population.longest_path().edges)
        self.main.apply_btn.setText('Apply')
        self.main.progressBar.hide()

        self.main.reset_btn.setDisabled(False)
        self.main.next_btn.setDisabled(False)
        self.main.start_btn.setDisabled(False)
        self.main.stop_btn.setDisabled(False)
        self.main.apply_btn.setDisabled(True)

    def start_auto_click(self):
        if not self.thread.isRunning:
            self.thread.start()
        self.thread.activate('ENDLESS')

    def reset_click(self):
        self.main.reset_btn.setDisabled(True)
        self.main.next_btn.setDisabled(True)
        self.main.start_btn.setDisabled(True)
        self.main.stop_btn.setDisabled(True)
        self.main.apply_btn.setDisabled(False)
        self.main.graph_max_canvas.plot()
        self.main.graph_min_canvas.plot()
        self.main.history_canvas.plot([],[],[])
        self.main.size.setValue(2)
        self.main.iterations.setValue(100)
        self.main.mutation_prob.setValue(0.0010)
        self.iterations_limit = 100
        self.current_iteration = 1
        self.avg_hist = []
        self.max_hist = []
        self.min_hist = []
        self.population = Population()
        self.population.set_progress_bar(self.main.progressBar, self.main.progress_bar_text)
        self.thread.stop()

