from Algorithm import Population

class ApplicationLogic():
    def __init__(self, main_window):
        self.main = main_window
        self.population = Population()

    def apply_click(self):
        self.population.set_parameters(
            size=self.main.size.value(),
            iterations=self.main.iterations.value(),
            mutation_prob=self.main.mutation_prob.value()
        )

        self.main.graph_max_canvas.set_nodes(self.population.cities)
        self.main.graph_min_canvas.set_nodes(self.population.cities)

        self.main.graph_max_canvas.plot(self.population.shortest_path().edges)
        self.main.graph_min_canvas.plot(self.population.longest_path().edges)
