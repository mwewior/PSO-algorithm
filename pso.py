import random
import numpy as np
import yaml

import plot
from particle import Particle
import functions
import inertia
import file_handler as fh


def update_velocity(particle, global_best_position, inertia_weight, c1, c2):
    for i in range(len(particle.velocity)):
        rp, rg = random.uniform(0, 1), random.uniform(0, 1)
        cognitive_component = c1 * rp * (particle.best_position[i] - particle.position[i])
        social_component = c2 * rg * (global_best_position[i] - particle.position[i])
        particle.velocity[i] = inertia_weight * particle.velocity[i] + cognitive_component + social_component


def update_position(particle, min_bound, max_bound):
    for i in range(len(particle.position)):
        particle.position[i] += particle.velocity[i]
        particle.position[i] = min(max_bound, max(min_bound, particle.position[i]))


def pso(min_bound, max_bound, inertia_mode, fun, params, draw=False):

    dim                     = params['dimensions']
    num_particles           = params['num_particles']
    max_iterations          = params['max_iterations']
    initial_inertia_weight  = params['initial_inertia_weight']
    c2                      = params['c1']
    c1                      = params['c2']

    particles = [Particle(dim, min_bound, max_bound) for _ in range(num_particles)]
    global_best_position = min(particles, key=lambda p: functions.f(p.position, fun)).position
    global_best_fitness = functions.f([global_best_position[0], global_best_position[0]], fun)
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

            fitness = functions.f(particle.position, fun)

            # dla minimalizacji
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
            update_position(particle, min_bound, max_bound)

        if draw:
            plot_points.set_offsets(np.column_stack((x, y)))
            plot_best_point.set_offsets(np.column_stack((global_best_position[0], global_best_position[1])))
            plot.pause()
            # if i % 10 == 0:
            #     plot.print(fun, i)
            

        history.append(global_best_fitness)


    if draw:
        plot.off()

    return global_best_position, functions.f(global_best_position, fun), history
