import pso
import plot
import numpy as np

def f(x, fun):
    if fun == 1:
        return sum(xi ** 2 for xi in x)
    elif fun == 2: # booth
        return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2
    elif fun == 3: # rosenbrock
        return (100.0 * (x[1] - x[0]**2)**2 + (1 - x[0])**2)
    elif fun == 4: # ackley
        n = len(x)
        sum1 = sum(xi**2 for xi in x)
        sum2 = sum(np.cos(2.0 * np.pi * xi) for xi in x)
        return -20.0 * np.exp(-0.2 * np.sqrt(sum1 / n)) - np.exp(sum2 / n) + 20 + np.exp(1)
    elif fun == 5: # michalewicz
        m = 10    
        return -np.sin(x[0]) * np.sin(x[0]**2 / np.pi)**(2 * m) - np.sin(x[1]) * np.sin(2 * x[1]**2 / np.pi)**(2 * m)
    elif fun == 6: # holder_table
        return -abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(abs(1 - np.sqrt(x[0]**2 + x[1]**2)/np.pi)))
    
def bounds(fun):
    if fun == 1:
        return -5,5
    elif fun == 2: # booth
        return -10, 10
    elif fun == 3: # rosenbrock
        return  -5, 10
    elif fun == 4: # ackley
        return  -32.768, 32.768
    elif fun == 5: # michalewicz
        return 0, np.pi
    elif fun == 6: # holder_table
        return -10, 10
    
if __name__=='__main__':

    # Parametry algorytmu PSO
    dimensions = 2
    num_particles = 25
    max_iterations = 150
    initial_inertia_weight = 0.72984
    c1 = 2.05
    c2 = 2.05

    fun = 6 # wybór funkcji :
            # 1 - wielomianowa  - f(x) = 0 x = (0, 0)
            # 2 - booth - f(x) = 0 x = (1, 3)
            # 3 - rosenbrock - f(x) = 0 x = (0, 0)
            # 4 - ackley  - f(x) = -1.8013 x = (2.20, 1.57)
            # 5 - michalewicz - f(x) = 0 x = (0, 0)
            # 6 - holder_table - f(x) = -19.2085 x = (8.05502, 9.66459), x = (-8.05502, 9.66459), x = (8.05502, -9.66459), x = (-8.05502, -9.66459)
    min_bound, max_bound = bounds(fun)

    draw_online = 0 # czy rysować online
    draw_result = 1 # czy narysować wynik

    inertia_mode = 1

    num_tests = 200 #200
    best_fitnesses = []

    for _ in range(num_tests):
        # Uruchomienie algorytmu PSO
        best_position, best_fitness, history = pso.pso(dimensions, num_particles, max_iterations, min_bound, max_bound, initial_inertia_weight, inertia_mode, c1, c2, fun, draw_online)
        best_fitnesses.append(best_fitness)
    if draw_result:
        plot.draw_result(best_position, best_fitness, min_bound, max_bound, fun)
    trash_num = int(0.05*num_tests)
    average = sum(sorted(best_fitnesses)[trash_num:-trash_num])/(num_tests - trash_num)
    # print(sorted(best_fitnesses))
    print(f'Average best fitness = {average} for mode {inertia_mode}')


