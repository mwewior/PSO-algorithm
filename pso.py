import random
import numpy as np
import plot
from particle import Particle
import main
import inertia



def update_velocity(particle, global_best_position, inertia_weight, c1, c2):
    for i in range(len(particle.velocity)):
        rp, rg = random.uniform(0, 1), random.uniform(0, 1)
        cognitive_component = c1 * rp * (particle.best_position[i] - particle.position[i])
        social_component = c2 * rg * (global_best_position[i] - particle.position[i])
        particle.velocity[i] = inertia_weight * particle.velocity[i] + cognitive_component + social_component

def update_position(particle):
    for i in range(len(particle.position)):
        particle.position[i] += particle.velocity[i]

def pso(dim, num_particles, max_iterations, min_bound, max_bound, initial_inertia_weight, inertia_mode, c1, c2, fun=1, draw=0):
    particles = [Particle(dim, min_bound, max_bound) for _ in range(num_particles)]
    global_best_position = min(particles, key=lambda p: main.f(p.position, fun)).position
    global_best_fitness = main.f([global_best_position[0], global_best_position[0]], fun)
    history = []

    if draw:
        plot_points, plot_best_point = plot.draw_online(min_bound, max_bound, fun)

    for i in range(max_iterations):
        x = []
        y = []
        for particle in particles:
            if draw:
                x.append(particle.position[0])
                y.append(particle.position[1])

            fitness = main.f(particle.position, fun)

            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position.copy()

            if fitness < global_best_fitness:
                global_best_position = particle.position.copy()
                global_best_fitness = fitness

        for particle in particles:
            if inertia_mode == 1:
                inertia_weight = initial_inertia_weight
            elif inertia_mode == 2:
                inertia_weight = inertia.mode2(i, max_iterations, initial_inertia_weight)
            elif inertia_mode == 3:
                inertia_weight = inertia.mode3(particle.best_fitness, global_best_fitness, initial_inertia_weight)
            update_velocity(particle, global_best_position, inertia_weight, c1, c2)
            update_position(particle)
        if draw:
            plot_points.set_offsets(np.column_stack((x, y)))
            plot_best_point.set_offsets(np.column_stack((global_best_position[0], global_best_position[1])))
            plot.pause()

        history.append(global_best_position)
    if draw:
        plot.off()


    return global_best_position, main.f(global_best_position, fun), history
