import itertools
from math import factorial
import random
from numpy.random import choice
from GraphObjects import Path
from settings import *


class Population:
    def __init__(self):
        self.cities = CITIES
        self.MAX_SIZE = factorial(len(self.cities))
        self.size = 0
        self.iterations = 0
        self.mutation_prob = 0.001
        self.paths = []  # <-- Population
        self.is_initialized = False
        self.progress_bar = None
        self.progress_bar_text = None
        self.current_iteration = 1
        self.iteration_limit = 1

    def set_progress_bar(self, progress_bar, progress_bar_text):
        self.progress_bar = progress_bar
        self.progress_bar_text = progress_bar_text

    def set_iteration_limit(self, iteration_limit):
        self.iteration_limit = iteration_limit

    def set_parameters(self, size=0, iterations=0, mutation_prob=0.001):
        self.progress_bar_text.setText('Applying parameters...')
        self.size = (size if size <= self.MAX_SIZE else self.MAX_SIZE) if size > 0 else 0
        self.iterations = iterations
        self.mutation_prob = mutation_prob
        print('--Zaczynam generować')
        self.progress_bar_text.setText('Generating paths...')
        self.paths = self.generate_n_paths(size)
        print('--Wygenerowałem')
        if size and iterations:
            self.is_initialized = True
        self.progress_bar_text.setText('Ready!')

    def generate_n_paths(self, n):
        def random_paths():
            i = 0
            while i < n:
                random_cities = random.sample(self.cities, len(self.cities))
                yield tuple(random_cities + [random_cities[0]])
                i += 1

        return [Path(path) for path in random_paths()]

    def reproduce(self):
        values = [1/path.length for path in self.paths]  # TODO zmienic funkcje przystosowania na tę z wykładu
        sum_values = sum(values)
        roulette = dict()

        for i, path in enumerate(self.paths):
            roulette[path.id] = values[i] / sum_values
        probabilities = [roulette[path.id] for path in self.paths]
        self.paths = choice(self.paths, self.size, p=probabilities)
        return self

    def cross(self):
        if self.size <= 1:
            return self
        pairs = []
        tmp_items = list(self.paths.copy())

        while len(tmp_items) > 1:
            r1 = tmp_items.pop(random.randrange(0, len(tmp_items)))
            r2 = tmp_items.pop(random.randrange(0, len(tmp_items)))
            pairs.append((r1, r2))

        crossed = []

        for pair in pairs:
            a, b = pair[0].nodes, pair[1].nodes
            const_positions, i, stop, item = [], 0, a[0], None
            while item != stop:
                const_positions.append(i)
                item = b[i]
                i = a.index(item)
            crossed.append(Path([a[i] if i in const_positions else b[i] for i in range(len(a))]))
            crossed.append(Path([b[i] if i in const_positions else a[i] for i in range(len(b))]))

        self.paths = crossed
        return self

    def mutate(self):
        new_paths = []
        for path in self.paths:
            for i in range(len(path.nodes)):
                x = random.uniform(0, 1)
                if x <= self.mutation_prob:
                    pos = i
                    while pos == i:
                        pos = random.randrange(0, len(path.nodes))
                        if pos != i:
                            path.swap(i, pos)
            path.update_edges()
            new_paths.append(path)
        self.paths = new_paths
        return self

    def shortest_path(self):
        shortest_path = self.paths[0]
        min_length = 9999999
        for path in self.paths:
            if path.length < min_length:
                min_length = path.length
                shortest_path = path
        return shortest_path

    def average_path_length(self):
        return sum([path.length for path in self.paths])/len(self.paths)

    def longest_path(self):
        longest_path = self.paths[0]
        max_length = 0
        for path in self.paths:
            if path.length > max_length:
                max_length = path.length
                longest_path = path
        return longest_path

if __name__ == "__main__":
    print('Start!')
    p = Population()
    print('Stworzyłem pustą populacje')
    p.set_parameters(size=100, iterations=1000)
    print('Zainicjalizowałem populacje')
    print(p.paths)
    print('Wyświetliłem')
    print('Sprawdzam reprodukcje')
    for i in range(50):
        print(p.paths)
        p.reproduce()
    print(p.paths)
