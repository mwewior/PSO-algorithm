import time
import numpy as np
import statistics
import pso
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
    worst_fitness = max(best_fitnesses)
    best_best_fitness = min(best_fitnesses)
    delete_index = sorted(range(len(best_fitnesses)), key=lambda i: best_fitnesses[i], reverse=True)[:int(len(best_fitnesses)*0.05)]
    delete_index = sorted(delete_index, reverse=True)
    # Usuń odpowiednie elementy z każdej listy
    for index in delete_index:
        del best_fitnesses[index]
        del times[index]
        del histories[index]

    return best_fitnesses, times, histories, worst_fitness, best_best_fitness


def make_test(f_ammount, inertia_modes, params):

    values = []
    times = []
    average = []
    deviation_val = []
    deviation_prcnt = []
    histories = []
    worst_fitness = []
    best_fitness = []

    for f_id in range(f_ammount):

        values.append([])
        times.append([])
        average.append([])
        deviation_val.append([])
        deviation_prcnt.append([])
        histories.append([])
        worst_fitness.append([])
        best_fitness.append([])

        for mode in range(inertia_modes):

            test_values, test_times, history, worst_fit, best_fit = benchmark(params, f_id+1, mode+1)

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
            worst_fitness[f_id].append(worst_fit)
            best_fitness[f_id].append(best_fit)

    results = {
        "values": values,
        "mean": average,
        "standard deviation": deviation_val,
        "percentage deviation": deviation_prcnt,
        "times": times,
        "histories_means": histories,
        "worst_fitness": worst_fitness,
        "best_fitness": best_fitness
    }

    return results


if __name__ == '__main__':
    print("benchmark started")
    param_path = "./parameters/general_params.yaml"
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
