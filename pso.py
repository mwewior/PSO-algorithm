import random
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import math
from particle import Particle


def f(x):
    x, y = x[0], x[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    # 5*math.e**2-4*math.e*x1+x1**2+2*math.e*x2+x2**2
    # return sum(xi ** 2 for xi in x)

def update_velocity(particle, global_best_position, inertia_weight, c1, c2):
    for i in range(len(particle.velocity)):
        rp, rg = random.uniform(0, 1), random.uniform(0, 1)
        cognitive_component = c1 * rp * (particle.best_position[i] - particle.position[i])
        social_component = c2 * rg * (global_best_position[i] - particle.position[i])
        particle.velocity[i] = inertia_weight * particle.velocity[i] + cognitive_component + social_component

def update_position(particle):
    for i in range(len(particle.position)):
        particle.position[i] += particle.velocity[i]

def pso(dim, num_particles, max_iterations, min_bound, max_bound, inertia_weight, c1, c2, points, best_point):
    particles = [Particle(dim, min_bound, max_bound) for _ in range(num_particles)]
    global_best_position = min(particles, key=lambda p: f(p.position)).position
    global_best_fitness = f([global_best_position[0], global_best_position[0]])
    history = []

    for _ in range(max_iterations):
        x = []
        y = []
        for particle in particles:
            x.append(particle.position[0])
            y.append(particle.position[1])
             # Aktualizacja danych punktów na wykresie

            # plt.scatter([particle.position[0]], [particle.position[1]], color='r', s=10, label='Best Position')
            fitness = f(particle.position)

            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position.copy()

            if fitness < global_best_fitness:
                global_best_position = particle.position.copy()
                global_best_fitness = fitness

        for particle in particles:
            update_velocity(particle, global_best_position, inertia_weight, c1, c2)
            update_position(particle)
        # Oczekiwanie na chwilę, aby zobaczyć zmiany
        # plt.scatter([global_best_particle.best_position[0]], [global_best_particle.best_position[1]], color='g', s=20, label='Best Position')
        points.set_offsets(np.column_stack((x, y)))
        best_point.set_offsets(np.column_stack((global_best_position[0], global_best_position[1])))

        plt.pause(0.1)
        # plt.clf()
        # plt.contourf(X,Y,Z, cmap='viridis', levels=100)

        history.append(global_best_position)

    return global_best_position, f(global_best_position), history
