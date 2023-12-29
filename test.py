import numpy as np

# while 1:
#     dif = liczba = np.random.uniform(0, 30)
#     # Normalizacja do przedziału od 0 do 2
#     print((dif/(dif+1)))
#     inertia_weight = 0.7*(dif/(dif+1))

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def michalewicz_function_2d(x, y, m=10):
    return -np.sin(x) * np.sin(x**2 / np.pi)**(2 * m) - np.sin(y) * np.sin(2 * y**2 / np.pi)**(2 * m)

# Define the range for x and y
x_range = np.linspace(0, np.pi, 100)
y_range = np.linspace(0, np.pi, 100)

# Create a mesh grid from x and y
x_mesh, y_mesh = np.meshgrid(x_range, y_range)

# Evaluate the Michalewicz function for each point in the mesh grid
z_mesh = michalewicz_function_2d(x_mesh, y_mesh)

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_mesh, y_mesh, z_mesh, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Michalewicz Function Value')

plt.title('Michalewicz Function in 2D')
plt.show()
