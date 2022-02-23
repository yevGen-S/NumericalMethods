import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from decimal import Decimal


def func(x):
    return x * np.sin(np.pi * x)


def integration3_8_recursive(f, a, b, eps):
    I_prev = (f(a) + 3 * f((2 * a + b) / 3) +
              3 * f((a + 2 * b) / 3) + f(b)) * (b - a) / 8

    I = ((f(a) + 3 * f((2 * a + (a + b) / 2) / 3) + 3 * f((a + 2 * (a + b) / 2) / 3) + f((a + b) / 2)) * (
            (a + b) / 2 - a)) / 8 \
        + (f(a) + 3 * f((2 * (a + b) / 2 + b) / 3) + 3 * f(((a + b) / 2 + 2 * b) / 3) + f(b)) * (b - (a + b) / 2) / 8


    if (abs(I - I_prev) / (2 ** 4 - 1)) < eps:
        return I_prev

    return integration3_8_recursive(f, a, (a + b) / 2, eps) + integration3_8_recursive(f, (a + b) / 2, b, eps)


def integration3_8(f, a, b, eps):
    def integration_body(number_of_nodes):
        x_grid = np.linspace(a, b, number_of_nodes)
        n = len(x_grid)
        I = 0
        for i in range(1, n):
            I += (f(x_grid[i - 1]) + 3 * f((2 * x_grid[i - 1] + x_grid[i]) / 3) +
                  3 * f((x_grid[i - 1] + 2 * x_grid[i]) / 3) + f(x_grid[i])) * (x_grid[i] - x_grid[i - 1]) / 8
        return I

    incrementer = lambda i: i + (i - 1)
    n = 2
    number_of_nodes_arr = []
    I_prev = integration_body(n)
    n = incrementer(n)
    number_of_nodes_arr.append(n)
    I = integration_body(n)
    err = []
    err.append(abs(I - I_prev) / (2 ** 4 - 1))
    while (abs(I - I_prev) / (2 ** 4 - 1)) > eps:
        err.append(abs(I - I_prev) / (2 ** 4 - 1))
        I_prev = I
        n = incrementer(n)
        I = integration_body(n)
        number_of_nodes_arr.append(n)

    return I, err, number_of_nodes_arr


def fun(x):
    return np.exp(x)


print(integration3_8(fun, a=0, b=1, eps=1e-15))
print(integrate.quad(fun, a=0, b=1))
