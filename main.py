import time
import yaml
import numpy as np

import pso
import plot
import functions
import file_handler as fh


def benchmark(param_path, fun, inertia_mode):

    common_params = fh.get_yaml_params(param_path, "common")
    specific_params = fh.get_yaml_params(param_path, "specific")
    num_tests    =  common_params['num_tests']

    # inertia_mode =  specific_params['inertia_mode']
    # fun          =  specific_params['fun']

    min_bound, max_bound = functions.bounds(fun)

    best_fitnesses = []
    times = []

    for _ in range(num_tests):
        # Uruchomienie algorytmu PSO

        start_time = time.time()
        best_position, best_fitness, history = pso.pso(min_bound, max_bound, inertia_mode, fun, param_path, False)
        end_time = time.time()
        elapsed_time = end_time - start_time

        best_fitnesses.append(best_fitness)
        times.append(elapsed_time)

    return best_fitnesses, times


if __name__ == '__main__':

    param_path = "./parameters/edit_params.yaml"
    save_file_path = "./results/param_json.json"

    f_ammount = 6
    inertia_modes = 3
    values = []
    times = []

    for f_id in range(f_ammount):
        values.append([])
        times.append([])
        for mode in range(inertia_modes):
            test_values, test_times = benchmark(param_path, f_id+1, mode+1)
            values[f_id].append(test_values)
            times[f_id].append(test_times)

    results = {
        "values": values,
        "times": times
    }

    fh.save_results(save_file_path, results)
    print("benchmark ended")

"""
if __name__ == '__main__':

    param_path = "./parameters/edit_params.yaml"
    common_params = fh.get_yaml_params(param_path, "common")
    specific_params = fh.get_yaml_params(param_path, "specific")

    draw_online  =  common_params['draw_online']   # czy rysować online
    draw_result  =  common_params['draw_result']   # czy narysować wynik
    num_tests    =  common_params['num_tests']

    inertia_mode =  specific_params['inertia_mode']
    fun          =  specific_params['fun']

    min_bound, max_bound = functions.bounds(fun)

    best_fitnesses = []
    start_time = time.time()

    for _ in range(num_tests):
        # Uruchomienie algorytmu PSO
        best_position, best_fitness, history = pso.pso(min_bound, max_bound, inertia_mode, fun, param_path, draw_online)
        best_fitnesses.append(best_fitness)

    end_time = time.time()
    elapsed_time = end_time - start_time

    trash_num = int(0.05 * num_tests)
    average = sum(sorted(best_fitnesses)[trash_num:-trash_num])/(num_tests - trash_num)

    if draw_result:
        plot.draw_result(best_position, best_fitness, min_bound, max_bound, fun)
"""