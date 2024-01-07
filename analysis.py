# plot_convergence.py
import json
import matplotlib.pyplot as plt

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def plot_convergence(data):
    benchmark_data = data.get('benchmark', {})
    tests = benchmark_data.get('tests', [])

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
                plt.plot(iterations, mean_fitness, label=f'Mode {mode}')

            plt.title(f'Krzywa zbiegania - Funkcja {f_id} ({function_type})')
            plt.xlabel('Iteracje')
            plt.ylabel('Funkcja celu')
            plt.legend()
            plt.show()


def krzywa_zbiegania():
    file_path = './results/param_json.json'  # Podaj ścieżkę do swojego pliku z wynikami
    results_data = read_json(file_path)
    plot_convergence(results_data)
    

krzywa_zbiegania()
