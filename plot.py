import matplotlib.pyplot as plt
import numpy as np
import functions


def draw_grid(min_bound, max_bound, fun):
     # Rysowanie funkcji celu
    step = abs(max_bound - min_bound)/1000
    X, Y = np.meshgrid(np.arange(min_bound,max_bound, step) , np.arange(min_bound,max_bound, step) )

    Z = functions.f([X, Y], fun)

    fig = plt.figure()

    contour = plt.contourf(X,Y,Z, cmap='viridis', levels=100)

    # Dodanie kolorowej skali
    cbar = plt.colorbar(contour)
    cbar.set_label('Trzecia zmienna')

    plt.xlabel('X')
    plt.ylabel('Y')


def draw_online(min_bound, max_bound, fun):
    plt.ion()

    draw_grid(min_bound, max_bound, fun)

    # Wyświetlenie punktów
    plot_points = plt.scatter([], [], c='r', marker='o')
    plot_best_point = plt.scatter([], [], c='g', marker='o')

    plt.show()
    return plot_points, plot_best_point


def draw_result(best_position, best_fitness, min_bound, max_bound, fun):
    draw_grid(min_bound, max_bound, fun)
    plt.scatter([best_position[0]], [best_position[1]], color='w', s=50, label='Best Position')
    plt.show()


def off():
    plt.ioff()


def pause():
    plt.pause(0.1)

def print(fun,i):
    plt.savefig(f'./wykresy/przebiegi/1przebieg{fun}_iter{i}.png', format='png')