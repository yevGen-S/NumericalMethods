import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
from math import *

# CONDITIONS
pi = 3.1416
a = 0
b = 20
x_values = []
x_full_interval = np.linspace(a, b, 100)
n = 20


def chebyshev_grid(a, b, n):
    return np.array([(b - a) * 0.5 * cos(pi * (2 * i + 1) / (2 * n))
                     + (a + b) * 0.5 for i in range(n)])


# FUNCTIONS
def func(x):
    return x * np.sin(pi * x)


def func_abs(x):
    return abs(x * np.sin(pi * x))


def lagrange(x_uniform_grid, fun):
    def lagrange_body(x):
        sum = 0
        for i, xi in enumerate(x_uniform_grid):
            val = 1
            for k, xk in enumerate(x_uniform_grid):
                if i == k:
                    continue
                val *= (x - xk) / (xi - xk)
            val *= fun(xi)
            sum += val
        return sum

    return lagrange_body


def graph(number_of_nodes):
    a = 0
    b = 20
    x_uniform_grid = np.linspace(a, b, n)
    x_chebyshev = chebyshev_grid(a, b, n)
    fun_lagrange = lagrange(x_uniform_grid, func)
    fun_chebyshek = lagrange(x_chebyshev, func)

    x_intreval2 = np.linspace(a, b, 100)
    # GRAPHICS
    plt.grid()
    plt.title(f"function nodes in grid = {number_of_nodes}")
    plt.figure(1)
    plt.plot(x_intreval2, func(x_intreval2), linewidth=2, label='function')
    plt.plot(x_intreval2, fun_lagrange(x_intreval2), linewidth=2, marker='*', label='interpolation')
    plt.plot(x_intreval2, fun_chebyshek(x_intreval2), linewidth=1, color='black', label='chebyshek')
    plt.scatter(x_uniform_grid, func(x_uniform_grid), marker='d', linewidths=5, color='red')
    plt.scatter(x_chebyshev, func(x_chebyshev), linewidths=5, marker='o', color='green')
    plt.legend()


# # abs
# fun_lagrange_abs = lagrange(x_uniform_grid, func_abs)
# fun_chebyshek_abs = lagrange(x_chebyshev, func_abs)
#
# plt.grid()
# plt.title("function_abs")
# plt.figure(100)
# plt.plot(x_full_interval, func_abs(x_full_interval), linewidth=2, label='function_abs')
# plt.plot(x_full_interval, fun_lagrange_abs(x_full_interval), linewidth=2, marker='*', label='interpolation')
# plt.plot(x_full_interval, fun_chebyshek_abs(x_full_interval), linewidth=1, color='black', label='chebyshek')
# plt.scatter(x_uniform_grid, func_abs(x_uniform_grid), marker='d', linewidths=5, color='red')
# plt.scatter(x_chebyshev, func_abs(x_chebyshev), linewidths=5, marker='o', color='green')
# plt.legend()


# Interpolation accuracy of number of nodes.

def accuracy_of_nodes_number_uniform_grid(number_of_nodes):
    plt.figure(2)
    plt.title("Accuracy of nodes number in uniform grid")
    plt.plot(x_full_interval, func(x_full_interval), label='function: x * sin(pi * x)', linewidth=3, marker='o',
             color='red')
    for i in range(number_of_nodes, 3, -1):
        x_uniform = np.linspace(a, b, i)
        lagrange_polynom = lagrange(x_uniform, func)
        if i == number_of_nodes:
            plt.plot(x_full_interval, lagrange_polynom(x_full_interval), label=f'{i} узлов ', linewidth=1.5,
                     color='black', marker='*')
            continue
        plt.plot(x_full_interval, lagrange_polynom(x_full_interval), label=f'{i} узлов ', linewidth=0.5, marker=',')
    plt.grid()
    plt.legend()


def accuracy_of_nodes_number_chebyshev_grid(number_of_nodes):
    plt.figure(3)
    plt.title("Accuracy of nodes number in chebyshev grid")
    plt.plot(x_full_interval, func(x_full_interval), label='function: x * sin(pi * x)', linewidth=3, marker='o',
             color='red')
    for i in range(number_of_nodes, 3, -1):
        x_chebysh = chebyshev_grid(a, b, i)
        lagrange_polynom = lagrange(x_chebysh, func)
        if i == number_of_nodes:
            plt.plot(x_full_interval, lagrange_polynom(x_full_interval), label=f'{i} узлов ', linewidth=1.5,
                     color='black', marker='*')
            continue
        plt.plot(x_full_interval, lagrange_polynom(x_full_interval), label=f'{i} узлов ', linewidth=0.5, marker=',')
    plt.grid()
    plt.legend()


def error_of_number_of_nodes(number_of_nodes):
    a1 = -3
    b1 = 3
    x_full_interval2 = np.linspace(a1, b1, 100)

    plt.figure(4)
    plt.title("Absolute error of number of nodes in grid")
    plt.grid()
    number_of_nodes_array = []
    uniform_grid_err_array = []
    chebysh_grid_err_array = []

    for i in range(number_of_nodes, 100, 5):
        number_of_nodes_array.append(i)
        x_uniform = np.linspace(a1, b1, i)
        x_chebysh = chebyshev_grid(a1, b1, i)

        lagrange_uniform_grid = lagrange(x_uniform, func)
        lagrange_chebysh_grid = lagrange(x_chebysh, func)
        uniform_grid_err_array.append(
            max([abs(func(xi) - lagrange_uniform_grid(xi)) for xi in x_full_interval2]))
        chebysh_grid_err_array.append(
            max([abs(func(xi) - lagrange_chebysh_grid(xi)) for xi in x_full_interval2]))

    plt.grid()
    plt.yscale('log')
    plt.plot(number_of_nodes_array, uniform_grid_err_array, label='Lagrange interpolation for uniform grid')
    plt.plot(number_of_nodes_array, chebysh_grid_err_array, label='Lagrange interpolation for chebysh grid')
    plt.legend()


def accuracy_of_grid(number_of_nodes):
    plt.figure(5)
    plt.title(f"Accuracy of grid \n number of nodes in grids = {number_of_nodes}")
    x_uniform = np.linspace(a, b, number_of_nodes)
    x_chybyshev = chebyshev_grid(a, b, number_of_nodes)
    fun_lagrang = lagrange(x_uniform, func)
    fun_chebysh = lagrange(x_chybyshev, func)
    plt.plot(x_full_interval, func(x_full_interval), linewidth=2, label='function: x * sin(pi*x)')
    plt.plot(x_full_interval, fun_lagrang(x_full_interval), linewidth=1.5, marker='*', label='lagrange on uniform grid')
    plt.plot(x_full_interval, fun_chebysh(x_full_interval), linewidth=1.5, label='lagrange on chebyshev')
    plt.scatter(x_uniform, func(x_uniform), marker='d', linewidths=5)
    plt.scatter(x_chybyshev, func(x_chybyshev), linewidths=5, marker='o')
    plt.legend()


def accuracy_of_number_of_nodes_animated():
    a1 = -10
    b1 = 10
    x_ful_local = np.linspace(a1, b1, 100)
    fig = plt.figure()
    ax = plt.axes()
    line, = ax.plot([], [], lw=1.5, label='lagrange interpolation uniform grid ', color='blue')
    line2, = ax.plot([], [], lw=1.5, label='lagrange interpolation chebyshev grid ', color='green')
    plt.scatter(x_ful_local, func(x_ful_local), marker='*', lw=0.3, label='function', color='red')

    # line2, = ax.plot([], [], lw=1, label=f'lagrange interpolation uniform grid\n number of nodes = ')

    def init():
        line.set_data([], [])
        line2.set_data([], [])
        return line, line2,

    def animate(i):
        x = x_full_interval
        text = plt.text(0, 0, f"number of nodes ={i}")
        x_grid = np.linspace(a1, b1, i)
        x_chebysh = chebyshev_grid(a1, b1, i)
        lagrange_uniform = lagrange(x_grid, func)
        lagrange_chebysh = lagrange(x_chebysh, func)
        y = lagrange_uniform(x_ful_local)
        y_ch = lagrange_chebysh(x_ful_local)
        line.set_data(x, y)
        line2.set_data(x, y_ch)
        return line, line2,

    anim = ani.FuncAnimation(fig, animate, init_func=init, frames=100, interval=800, blit=True)
    plt.legend()
    plt.grid()
    plt.show()


# accuracy_of_number_of_nodes_animated()
# accuracy_of_nodes_number_uniform_grid(13)
# accuracy_of_nodes_number_chebyshev_grid(13)
error_of_number_of_nodes(5)
# accuracy_of_grid(20)
plt.grid()
plt.show()
