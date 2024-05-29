# IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import time

# Visualize the convergence process
y_func = lambda x: x**2
y_deriv = lambda x: 2 * x

# Data for plotting
x = np.arange(-10, 10, 0.1)
y = y_func(x)

# Pick a random starting point
current_pos = (-8, y_func(-8))

# Init params
learning_rate = 0.1
n_epochs = 20

# Run algo
for epoch in range(n_epochs):
    new_x = current_pos[0] - learning_rate * y_deriv(current_pos[0])
    new_y = y_func(new_x)
    current_pos = (new_x, new_y)

    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color='red')
    plt.pause(0.001)
    plt.clf()

plt.show()