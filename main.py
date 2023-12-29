import pso
import plot
import math

def f(x, fun):
    x1, x2 = x[0], x[1]
    if fun == 1:
        return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2
    elif fun == 2:
        return 5*math.e**2-4*math.e*x1+x1**2+2*math.e*x2+x2**2
    elif fun == 3:
        return sum(xi ** 2 for xi in x)
    
if __name__=='__main__':

    # Parametry algorytmu PSO
    dimensions = 2
    num_particles = 20
    max_iterations = 100
    min_bound = -5.0
    max_bound = 5.0
    initial_inertia_weight = 0.72984
    c1 = 2.05
    c2 = 2.05
    fun = 3 # wybór funkcji 
    draw_online = 1 # czy rysować online
    draw_result = 1 # czy narysować wynik
    plot_points, plot_best_point = 0,0

    inertia_mode = 3




    # Uruchomienie algorytmu PSO
    best_position, best_fitness, history = pso.pso(dimensions, num_particles, max_iterations, min_bound, max_bound, initial_inertia_weight, inertia_mode, c1, c2, fun, draw_online)

    if draw_result:
        plot.draw_result(best_position, best_fitness, min_bound, max_bound, fun)

    print(f'Best position = {best_position} and best fitness = {best_fitness}')


