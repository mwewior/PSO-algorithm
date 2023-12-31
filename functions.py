import numpy as np


def f(x, fun):
    if fun == 1:
        return sum(xi ** 2 for xi in x)
    elif fun == 2:   # booth
        return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2
    elif fun == 3:   # rosenbrock
        return (100.0 * (x[1] - x[0]**2)**2 + (1 - x[0])**2)
    elif fun == 4:   # ackley
        n = len(x)
        sum1 = sum(xi**2 for xi in x)
        sum2 = sum(np.cos(2.0 * np.pi * xi) for xi in x)
        return -20.0 * np.exp(-0.2 * np.sqrt(sum1 / n)) - np.exp(sum2 / n) + 20 + np.exp(1)
    elif fun == 5:  # michalewicz
        m = 10
        return -np.sin(x[0]) * np.sin(x[0]**2 / np.pi)**(2 * m) - np.sin(x[1]) * np.sin(2 * x[1]**2 / np.pi)**(2 * m)
    elif fun == 6:   # holder_table
        return -abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(abs(1 - np.sqrt(x[0]**2 + x[1]**2)/np.pi)))


def bounds(fun):
    if fun == 1:
        return -5, 5
    elif fun == 2:  # booth
        return -10, 10
    elif fun == 3:  # rosenbrock
        return -5, 10
    elif fun == 4:  # ackley
        return -32.768, 32.768
    elif fun == 5:  # michalewicz
        return 0, np.pi
    elif fun == 6:  # holder_table
        return -10, 10


def names(fun):
    functions = {
        1: 'wielomian',
        2: 'booth',
        3: 'rosenbrock',
        4: 'ackley',
        5: 'michalewicz',
        6: 'holder table'
    }
    return functions[fun]
