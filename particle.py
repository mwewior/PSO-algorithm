import random


class Particle:
    def __init__(self, dim, min_bound, max_bound):
        self.position = [random.uniform(min_bound, max_bound) for _ in range(dim)]
        self.velocity = [random.uniform(-abs(max_bound - min_bound), abs(max_bound - min_bound)) for _ in range(dim)]
        self.best_position = self.position
        self.best_fitness = float('inf')
