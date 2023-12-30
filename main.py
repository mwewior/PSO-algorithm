import time
import yaml
import numpy as np

import pso
import plot
import functions


if __name__ == '__main__':

    # Parametry algorytmu PSO
    with open("params.yaml", "r") as pso_params:
        params = yaml.load(pso_params)

    inertia_mode =  params['inertia_mode']
    draw_online  =  params['draw_online']   # czy rysować online
    draw_result  =  params['draw_result']   # czy narysować wynik
    num_tests    =  params['num_tests']
    fun          =  params['fun']

    min_bound, max_bound = functions.bounds(fun)

    best_fitnesses = []


    print('program started')
    start_time = time.time()

    for _ in range(num_tests):
        # Uruchomienie algorytmu PSO
        best_position, best_fitness, history = pso.pso(min_bound, max_bound, inertia_mode, fun, draw_online)
        # best_position, best_fitness, history = pso.pso(dimensions, num_particles, max_iterations, min_bound, max_bound, initial_inertia_weight, inertia_mode, c1, c2, fun, draw_online)
        best_fitnesses.append(best_fitness)
        print(f'({_+1}) current iteration best fitness equals {best_fitness} for point {best_position}')

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f'algorithm took {elapsed_time} seconds')
    print(f'The test was run {num_tests} times')

    trash_num = int(0.05 * num_tests)
    average = sum(sorted(best_fitnesses)[trash_num:-trash_num])/(num_tests - trash_num)
    average2 = sum(sorted(best_fitnesses)) / num_tests

    print(f'Average best fitness = {average} for mode {inertia_mode}\n\t\t\t{average2}')

    if draw_result:
        plot.draw_result(best_position, best_fitness, min_bound, max_bound, fun)
