import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math





class Particle:
    def __init__(self, dim, min_bound, max_bound):
        self.position = [random.uniform(min_bound, max_bound) for _ in range(dim)]
        self.velocity = [random.uniform(-abs(max_bound - min_bound), abs(max_bound - min_bound)) for _ in range(dim)]
        self.best_position = self.position
        self.best_fitness = float('inf')

def f(x):
    x, y = x[0], x[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2 
    # 5*math.e**2-4*math.e*x1+x1**2+2*math.e*x2+x2**2
    # return sum(xi ** 2 for xi in x)

def update_velocity(particle, global_best_position, inertia_weight, c1, c2):
    for i in range(len(particle.velocity)):
        rp, rg = random.uniform(0, 1), random.uniform(0, 1)
        cognitive_component = c1 * rp * (particle.best_position[i] - particle.position[i])
        social_component = c2 * rg * (global_best_position[i] - particle.position[i])
        particle.velocity[i] = inertia_weight * particle.velocity[i] + cognitive_component + social_component

def update_position(particle):
    for i in range(len(particle.position)):
        particle.position[i] += particle.velocity[i]

def pso(dim, num_particles, max_iterations, min_bound, max_bound, inertia_weight, c1, c2):
    particles = [Particle(dim, min_bound, max_bound) for _ in range(num_particles)]
    global_best_position = min(particles, key=lambda p: f(p.position)).position
    global_best_fitness = f([global_best_position[0], global_best_position[0]])
    history = []
 
    
    


    for _ in range(max_iterations):
        x = []  
        y = [] 
        for particle in particles:
            x.append(particle.position[0]) 
            y.append(particle.position[1]) 
             # Aktualizacja danych punktów na wykresie
            
            # plt.scatter([particle.position[0]], [particle.position[1]], color='r', s=10, label='Best Position')
            fitness = f(particle.position)

            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position.copy()

            if fitness < global_best_fitness:
                global_best_position = particle.position.copy()
                global_best_fitness = fitness

        for particle in particles:
            update_velocity(particle, global_best_position, inertia_weight, c1, c2)
            update_position(particle)
        # Oczekiwanie na chwilę, aby zobaczyć zmiany
        # plt.scatter([global_best_particle.best_position[0]], [global_best_particle.best_position[1]], color='g', s=20, label='Best Position')
        points.set_offsets(np.column_stack((x, y)))
        best_point.set_offsets(np.column_stack((global_best_position[0], global_best_position[1])))

        plt.pause(0.1)
        # plt.clf()
        # plt.contourf(X,Y,Z, cmap='viridis', levels=100)

        history.append(global_best_position)

    return global_best_position, f(global_best_position), history


# Parametry algorytmu PSO
dimensions = 2
num_particles = 20
max_iterations = 100
min_bound = -5.0
max_bound = 5.0
inertia_weight = 0.7
c1 = 1.5
c2 = 1.5

plt.ion()

# Rysowanie funkcji celu
x = np.linspace(min_bound*2, max_bound*2, 100)
y = np.linspace(min_bound*2, max_bound*2, 100)
X, Y = np.meshgrid(np.arange(-5,5,0.01) , np.arange(-5,5,0.01) ) 

# X, Y = np.meshgrid(np.arange(-10,15,0.01) , np.arange(-15,10,0.01) )
Z = f([X, Y])

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
best_position, best_fitness, history = pso(dimensions, num_particles, max_iterations, min_bound, max_bound, inertia_weight, c1, c2)

# Oznaczenie znalezionego punktu
plt.scatter([best_position[0]], [best_position[1]], color='w', s=50, label='Best Position')


# Wyłączenie trybu interaktywnego (niezbędne, aby program zakończył się poprawnie)
plt.ioff()

# Wyświetlenie ostatecznego wykresu (opcjonalne, jeśli chcesz zobaczyć efekt końcowy)
plt.show()
