import json
import matplotlib.pyplot as plt
import numpy as np


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def krzywa_zbiegania(tests):

    for test in tests:
        common_params = test.get('common parameters', {})
        results = test.get('results', [])
        for result in results:
            f_id = result['f_id']
            function_type = result['function_type']

            for inertia_data in result['inertia']:
                mode = inertia_data['mode']
                mean_fitness = inertia_data['histories_means']

                iterations = list(range(1, len(mean_fitness) + 1))
                plt.plot(iterations, mean_fitness, label=f'tryb {mode+1}')

            plt.title(f'Krzywa zbiegania - Funkcja {f_id} ({function_type})')
            plt.xlabel('Iteracje')
            plt.ylabel('Funkcja celu')
            plt.legend()
            plt.savefig(f'./wykresy/krzywa_zbiegania{f_id}.png', format='png')
            plt.show()
            


def krzywa_ECDF(tests):
    for test in tests:
        common_params = test.get('common parameters', {})
        results = test.get('results', [])
        for result in results:
            f_id = result['f_id']
            function_type = result['function_type']

            plt.figure(figsize=(10, 6))
            
            for inertia_data in result['inertia']:
                mode = inertia_data['mode']
                mean_fitness = inertia_data['histories_means']
                sorted_data = np.sort(mean_fitness)
                ecdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
                plt.plot(sorted_data, ecdf, marker='.', linestyle='none', label=f'tryb {mode+1}')               
            plt.xlabel('Wartości danych')
            plt.ylabel('Dystrybuanta empiryczna')
            plt.title(f'Krzywa ECDF - Funkcja {f_id} ({function_type})')
            plt.legend()
            plt.savefig(f'./wykresy/krzywa_ecdf{f_id}.png', format='png')
            plt.show()


def box_plot(tests):

    for test in tests:
        common_params = test.get('common parameters', {})
        results = test.get('results', [])
        for result in results:
            f_id = result['f_id']
            function_type = result['function_type']
            values = []
            for inertia_data in result['inertia']:
                mode = inertia_data['mode']
                values.append(inertia_data['values'])
            data_sets = [np.array(values[1]), np.array(values[2])]
            plt.boxplot(data_sets, labels=['tryb 2', 'tryb 3'])
            plt.xlabel('Zbiory danych')
            plt.ylabel('Wartości danych')
            plt.title(f'Odchylenie standardowe - Funkcja {f_id} ({function_type})')
            plt.savefig(f'./wykresy/2box_plot{f_id}.png', format='png')
            plt.show()


def analiza():
    file_path = './results/param_json.json'
    results_data = read_json(file_path)
    benchmark_data = results_data.get('benchmark', {})
    tests = benchmark_data.get('tests', [])
    # krzywa_zbiegania(tests)
    # krzywa_ECDF(tests)
    box_plot(tests)

if __name__ == '__main__':
    analiza()