import itertools
from math import factorial
import random
from numpy.random import choice
from GraphObjects import Node, Path


class Population:
    def __init__(self):
        self.cities = {Node('A', 4, 4), Node('B', 1, 1), Node('C', 8, 9), Node('D', 2, 10), Node('E', 4, 10),
                       Node('F', 6, 9), Node('G', 5, 6), Node('H', 1, 8), Node('I', 8, 7), Node('J', 9, 4)}
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
        return [Path(permutations[i]) for i in random.sample(range(self.MAX_SIZE), self.size)]

    def reproduce(self):
        values = [path.length for path in self.paths]
        sum_values = sum(values)
        roulette = dict()

        for i, path in enumerate(self.paths):
            roulette[path.id] = values[i] / sum_values
        probabilities = [roulette[path.id] for path in self.paths]
        self.paths = choice(self.paths, self.size, p=probabilities)
        return self

    def cross(self):
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


if __name__ == "__main__":
    print('Start!')
    p = Population()
    print('Stworzyłem pustą populacje')
    p.set_parameters(size=4, iterations=1000)
    print('Zainicjalizowałem populacje')
    print(p.paths)
    print('Wyświetliłem')
    print('Sprawdzam crossing')
    print(p.paths)
    p.cross()
    print(p.paths)
