import pso
import plot
import numpy as np
import time
import yaml


def f(x, fun):
    if fun == 1:
        return sum(xi ** 2 for xi in x)
    elif fun == 2:   # booth
        return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2
    elif fun == 3:   # rosenbrock
        return (100.0 * (x[1] - x[0]**2)**2 + (1 - x[0])**2)
    elif fun == 4:   # ackley
        n = len(x)
        sum1 = sum(xi**2 for xi in x)
        sum2 = sum(np.cos(2.0 * np.pi * xi) for xi in x)
        return -20.0 * np.exp(-0.2 * np.sqrt(sum1 / n)) - np.exp(sum2 / n) + 20 + np.exp(1)
    elif fun == 5:  # michalewicz
        m = 10
        return -np.sin(x[0]) * np.sin(x[0]**2 / np.pi)**(2 * m) - np.sin(x[1]) * np.sin(2 * x[1]**2 / np.pi)**(2 * m)
    elif fun == 6:   # holder_table
        return -abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(abs(1 - np.sqrt(x[0]**2 + x[1]**2)/np.pi)))


def bounds(fun):
    if fun == 1:
        return -5, 5
    elif fun == 2:  # booth
        return -10, 10
    elif fun == 3:  # rosenbrock
        return -5, 10
    elif fun == 4:  # ackley
        return -32.768, 32.768
    elif fun == 5:  # michalewicz
        return 0, np.pi
    elif fun == 6:  # holder_table
        return -10, 10


if __name__ == '__main__':

    # Parametry algorytmu PSO
    with open("params.yaml", "r") as pso_params:
        params = yaml.load(pso_params, Loader=yaml.FullLoader)

    inertia_mode =  params['inertia_mode']
    draw_online  =  params['draw_online']   # czy rysować online
    draw_result  =  params['draw_result']   # czy narysować wynik
    num_tests    =  params['num_tests']
    fun          =  params['fun']

    min_bound, max_bound = bounds(fun)

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

    if draw_result:
        plot.draw_result(best_position, best_fitness, min_bound, max_bound, fun)

    trash_num = int(0.05 * num_tests)
    average = sum(sorted(best_fitnesses)[trash_num:-trash_num])/(num_tests - trash_num)

    average2 = sum(sorted(best_fitnesses)) / num_tests
    # print(sorted(best_fitnesses))

    print(f'Average best fitness = {average} for mode {inertia_mode}\n\t\t\t{average2}')
