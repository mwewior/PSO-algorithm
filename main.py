import time
import yaml
import numpy as np
import statistics

import pso
import plot
import functions
import file_handler as fh


def benchmark(params, fun, inertia_mode):

    num_tests    =  params['num_tests']
    draw_online    =  params['draw_online']

    # inertia_mode =  specific_params['inertia_mode']
    # fun          =  specific_params['fun']

    min_bound, max_bound = functions.bounds(fun)

    best_fitnesses = []
    times = []
    histories = []

    for _ in range(num_tests):
        # Uruchomienie algorytmu PSO

        start_time = time.time()
        best_position, best_fitness, history = pso.pso(min_bound, max_bound, inertia_mode, fun, params, draw_online)
        end_time = time.time()
        elapsed_time = end_time - start_time

        histories.append(history)

        best_fitnesses.append(best_fitness)
        times.append(elapsed_time)

    histories_mean = np.mean(histories, axis=0).tolist()

    return best_fitnesses, times, histories_mean


def make_test(f_ammount, inertia_modes, params):
    values = []
    times = []
    average = []
    deviation_val = []
    deviation_prcnt = []
    histories = []

    for f_id in range(f_ammount):

        values.append([])
        times.append([])
        average.append([])
        deviation_val.append([])
        deviation_prcnt.append([])
        histories.append([])

        for mode in range(inertia_modes):
        # for mode in range(1):

            test_values, test_times, histories_means = benchmark(params, f_id+1, mode+1)

            mean = statistics.fmean(test_values)
            variance = statistics.variance(test_values, mean)
            standard_deviation = np.sqrt(variance)
            std_dev_percent = abs(standard_deviation / mean) * 100

            # TODO
            # nie wiem czy to procentowe odchylenie ma sens
            # trzeba by to sprawdzić
            #
            # to chyba będzie do wywalenia
            # jeszcze trzeba dodoać wektor historii najlepszego rozwiązania
            # żeby zobaczyć która wersja jest najszybsza itd.
            # będzie trzeba jakieś dystrybuanty policzyć xD
            # coś tam na wykładzie 6 jest

            values[f_id].append(test_values)
            times[f_id].append(test_times)
            average[f_id].append(mean)
            deviation_val[f_id].append(standard_deviation)
            deviation_prcnt[f_id].append(std_dev_percent)
            histories[f_id].append(histories_means)

    results = {
        "values": values,
        "mean": average,
        "standard deviation": deviation_val,
        "percentage deviation": deviation_prcnt,
        "times": times,
        "histories_means": histories
    }

    return results


if __name__ == '__main__':
    print("benchmark started")
    param_path = "./parameters/edit_params.yaml"
    save_file_path = "./results/param_json.json"

    common_params = fh.get_yaml_params(param_path, "common")
    specific_params = fh.get_yaml_params(param_path, "specific")

    f_ammount = 6
    inertia_modes = 3

    start_time = time.time()

    results = make_test(f_ammount, inertia_modes, common_params)
    fh.save_results(save_file_path, results)

    end_time = time.time()
    test_time = end_time - start_time

    print("benchmark ended")
    print(f'took {test_time} seconds')


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