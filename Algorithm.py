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

    def set_parameters(self, size=0, iterations=0, mutation_prob=0.001):
        self.size = (size if size <= self.MAX_SIZE else self.MAX_SIZE) if size > 0 else 0
        self.iterations = iterations
        self.mutation_prob = mutation_prob
        print('--Zaczynam generować')
        self.paths = self.generate_n_paths(size)
        print('--Wygenerowałem')
        if size and iterations:
            self.is_initialized = True

    def generate_n_paths(self, n):
        print('----Tworzę listę permutacji')
        permutations = list(itertools.permutations(self.cities))
        print('----Stworzona')
        return [Path(permutations[x]) for x in random.sample(range(self.MAX_SIZE), self.size)]

    def reproduce(self):
        values = [path.length for path in self.paths]
        sum_values = sum(values)
        roulette = dict()

        for i, path in enumerate(self.paths):
            roulette[path.id] = values[i] / sum_values
        probabilities = [1 - roulette[path.id] for path in self.paths]
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
            crossed.append(Path(tuple([a[i] if i in const_positions else b[i] for i in range(len(a))])))
            crossed.append(Path(tuple([b[i] if i in const_positions else a[i] for i in range(len(b))])))

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
                        print('mutuje, i == {}, pos = {}'.format(i, pos))
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
    p.set_parameters(size=1, iterations=1000)
    print('Zainicjalizowałem populacje')
    print(p.paths)
    print('Wyświetliłem')
    print('Sprawdzam mutację')
    for i in range(200):
        print(p.paths)
        p.mutate()
    print(p.paths)
