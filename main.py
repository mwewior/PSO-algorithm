import time
import yaml
import numpy as np
import statistics
# import analysis
import pso
import plot
import functions
import file_handler as fh


def benchmark(params, fun, inertia_mode):

    num_tests    =  params['num_tests']
    draw_online    =  params['draw_online']

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



    return best_fitnesses, times, histories


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

            test_values, test_times, history = benchmark(params, f_id+1, mode+1)

            mean = statistics.fmean(test_values)
            variance = statistics.variance(test_values, mean)
            standard_deviation = np.sqrt(variance)
            std_dev_percent = abs(standard_deviation / mean) * 100
            histories_mean = np.mean(history, axis=0).tolist()

            values[f_id].append(test_values)
            times[f_id].append(test_times)
            average[f_id].append(mean)
            deviation_val[f_id].append(standard_deviation)
            deviation_prcnt[f_id].append(std_dev_percent)
            histories[f_id].append(histories_mean)

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

    # analysis.analiza()
