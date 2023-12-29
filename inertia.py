import numpy as np

def mode2(i, max_iterations, initial_inertia_weight):
## Współczynnik bezwładności zależny od czasu - malejący wraz z kolejnymi iteracjami algorytmu.
    inertia_weight = initial_inertia_weight*(i/max_iterations) +0.2
    return inertia_weight

def mode3(particle_best_fitness, global_best_fitness, initial_inertia_weight):
## Współczynnik bezwładności zależny od jakości rozwiązania.
    dif = particle_best_fitness - global_best_fitness

    inertia_weight = (initial_inertia_weight+0.1)*(dif/(dif+1))
    return inertia_weight