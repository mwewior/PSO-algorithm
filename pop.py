import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

class Particle:
    def __init__(self, dim, min_bound, max_bound):
        self.position = [random.uniform(min_bound, max_bound) for _ in range(dim)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dim)]
        self.best_position = self.position
        self.best_fitness = float('inf')

def objective_function(x):
    x1, x2 = x[0], x[1]
    return 5*math.e**2-4*math.e*x1+x1**2+2*math.e*x2+x2**2
    # return sum(xi ** 2 for xi in x)

def update_velocity(particle, global_best_position, inertia_weight, c1, c2):
    for i in range(len(particle.velocity)):
        r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
        cognitive_component = c1 * r1 * (particle.best_position[i] - particle.position[i])
        social_component = c2 * r2 * (global_best_position[i] - particle.position[i])
        particle.velocity[i] = inertia_weight * particle.velocity[i] + cognitive_component + social_component

def update_position(particle):
    for i in range(len(particle.position)):
        particle.position[i] += particle.velocity[i]

def pso(dim, num_particles, max_iterations, min_bound, max_bound, inertia_weight, c1, c2):
    particles = [Particle(dim, min_bound, max_bound) for _ in range(num_particles)]
    global_best_particle = min(particles, key=lambda p: objective_function(p.position))
    history = []

    for _ in range(max_iterations):
        for particle in particles:
            fitness = objective_function(particle.position)

            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position

            if fitness < objective_function(global_best_particle.position):
                global_best_particle = particle

        for particle in particles:
            update_velocity(particle, global_best_particle.position, inertia_weight, c1, c2)
            update_position(particle)

        history.append(global_best_particle.best_position)

    return global_best_particle.best_position, objective_function(global_best_particle.best_position), history

# Parametry algorytmu PSO
dimensions = 2
num_particles = 20
max_iterations = 100
min_bound = -5.0
max_bound = 5.0
inertia_weight = 0.7
c1 = 1.5
c2 = 1.5

# Uruchomienie algorytmu PSO
best_position, best_fitness, history = pso(dimensions, num_particles, max_iterations, min_bound, max_bound, inertia_weight, c1, c2)

# Rysowanie funkcji celu
x = np.linspace(min_bound, max_bound, 100)
y = np.linspace(min_bound, max_bound, 100)

X, Y = np.meshgrid(np.arange(-10,15,0.01) , np.arange(-15,10,0.01) )
Z = objective_function([X, Y])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolors='k')

# Rysowanie ścieżki algorytmu PSO
history = np.array(history).T
ax.plot(history[0], history[1], [objective_function(p) for p in history.T], color='r', marker='o', linestyle='dashed')

# Oznaczenie znalezionego punktu
ax.scatter([best_position[0]], [best_position[1]], [best_fitness], color='g', s=100, label='Best Position')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Objective Function Value')
ax.legend()

plt.show()
