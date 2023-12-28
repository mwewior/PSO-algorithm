from particle import Particle
import pso
import random
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import math


if __name__=='__main__':

    # Parametry algorytmu PSO
    dimensions = 2
    num_particles = 20
    max_iterations = 100
    min_bound = -5.0
    max_bound = 5.0
    inertia_weight = 0.7
    c1 = 1.5
    c2 = 0.1

    plt.ion()

    # Rysowanie funkcji celu
    x = np.linspace(min_bound*2, max_bound*2, 100)
    y = np.linspace(min_bound*2, max_bound*2, 100)
    X, Y = np.meshgrid(np.arange(-5,5,0.01) , np.arange(-5,5,0.01) )

    # X, Y = np.meshgrid(np.arange(-10,15,0.01) , np.arange(-15,10,0.01) )
    Z = pso.f([X, Y])

    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolors='k')
    contour = plt.contourf(X,Y,Z, cmap='viridis', levels=100)
    # # Rysowanie ścieżki algorytmu PSO
    # history = np.array(history).T
    # Wyświetlenie punktów
    points = plt.scatter([], [], c='r', marker='o')
    best_point = plt.scatter([], [], c='g', marker='o')



    # Dodanie kolorowej skali
    cbar = plt.colorbar(contour)
    cbar.set_label('Trzecia zmienna')


    # ax.plot(history[0], history[1], [f(p) for p in history.T], color='r', marker='o', linestyle='dashed')


    plt.xlabel('X')
    plt.ylabel('Y')
    # plt.set_zlabel('Objective Function Value')
    plt.legend()

    plt.show()

    # Uruchomienie algorytmu PSO
    best_position, best_fitness, history = pso.pso(dimensions, num_particles, max_iterations, min_bound, max_bound, inertia_weight, c1, c2, points, best_point)

    # Oznaczenie znalezionego punktu
    plt.scatter([best_position[0]], [best_position[1]], color='w', s=50, label='Best Position')


    # Wyłączenie trybu interaktywnego (niezbędne, aby program zakończył się poprawnie)
    plt.ioff()

    # Wyświetlenie ostatecznego wykresu (opcjonalne, jeśli chcesz zobaczyć efekt końcowy)
    plt.show()
