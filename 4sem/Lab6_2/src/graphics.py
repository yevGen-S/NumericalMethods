import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
from spline import cubic_spline, func
from chebyshev_grid import chebyshev_grid
from collections.abc import Iterable


def graph(left, right, number_of_nodes_in_grid):
    n = 1000
    x_full_interval = np.linspace(left, right, num=n)
    x_uniform = np.linspace(left, right, number_of_nodes_in_grid)
    x_chebysh = chebyshev_grid(left, right, number_of_nodes_in_grid)
    spline_chebysh = cubic_spline(x_chebysh, func)
    spline_uniform = cubic_spline(x_uniform, func)
    # scipy_cubic = CubicSpline(x_uniform, func(x_uniform))
    plt.figure(1)
    plt.title("Cubic splain")
    plt.plot(x_full_interval, func(x_full_interval), lw=3, label='starting function')
    plt.scatter(x_chebysh, func(x_chebysh), label='chebyshev grid', color='red',lw=5)
    plt.scatter(x_uniform, func(x_uniform), label='uniform grid', color='black')
    plt.plot(x_full_interval, spline_uniform(x_full_interval), label='spline on uniform')
    plt.plot(x_full_interval, spline_chebysh(x_full_interval), label='spline on chebyshev')
    # plt.plot(x_full_interval, scipy_cubic(x_full_interval), label='scipy implementation', color='green')
    plt.grid()
    plt.legend()


# def graph(number_of_nodes):
#     a = 0
#     b = 20
#     x_uniform_grid = np.linspace(a, b, n)
#     x_chebyshev = chebyshev_grid(a, b, n)
#     fun_lagrange = lagrange(x_uniform_grid, func)
#     fun_chebyshek = lagrange(x_chebyshev, func)
#
#     x_intreval2 = np.linspace(a, b, 100)
#     # GRAPHICS
#     plt.grid()
#     plt.title(f"function nodes in grid = {number_of_nodes}")
#     plt.figure(1)
#     plt.plot(x_intreval2, func(x_intreval2), linewidth=2, label='function')
#     plt.plot(x_intreval2, fun_lagrange(x_intreval2), linewidth=2, marker='*', label='interpolation')
#     plt.plot(x_intreval2, fun_chebyshek(x_intreval2), linewidth=1, color='black', label='chebyshek')
#     plt.scatter(x_uniform_grid, func(x_uniform_grid), marker='d', linewidths=5, color='red')
#     plt.scatter(x_chebyshev, func(x_chebyshev), linewidths=5, marker='o', color='green')
#     plt.legend()


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

def accuracy_of_nodes_number_uniform_grid(left, right, number_of_nodes_in_grid):
    n = 1000
    x_full_interval = np.linspace(left, right, num=n)
    plt.figure(2)
    plt.title("Accuracy of nodes number in uniform grid")
    plt.plot(x_full_interval, func(x_full_interval), label='function: x * sin(pi * x)',
             color='red')

    for i in range(number_of_nodes_in_grid, number_of_nodes_in_grid - 3, -1):
        x_uniform = np.linspace(left, right, i)
        spline = cubic_spline(x_uniform, func)
        if i == number_of_nodes_in_grid:
            plt.plot(x_full_interval, spline(x_full_interval), label=f'{i} узлов ', linewidth=2,
                     color='black')
            continue
        plt.plot(x_full_interval, spline(x_full_interval), label=f'{i} узлов ', linewidth=0.5)
    plt.grid()
    plt.legend()


def accuracy_of_nodes_number_chebyshev_grid(left, right, number_of_nodes_in_grid):
    n = 1000
    x_full_interval = np.linspace(left, right, num=n)
    plt.figure(3)
    plt.title("Accuracy of nodes number in chebyshev grid")
    plt.plot(x_full_interval, func(x_full_interval), label='function: x * sin(pi * x)', linewidth=2,
             color='red')
    for i in range(number_of_nodes_in_grid,number_of_nodes_in_grid-3, -1):
        x_chebysh = chebyshev_grid(left, right, i)
        spline_chebyshev_grid = cubic_spline(x_chebysh, func)
        if i == number_of_nodes_in_grid:
            plt.plot(x_full_interval, spline_chebyshev_grid(x_full_interval), label=f'{i} узлов ', linewidth=1,
                     color='black')
            continue
        plt.plot(x_full_interval, spline_chebyshev_grid(x_full_interval), label=f'{i} узлов ', linewidth=0.5)
    plt.grid()
    plt.legend()


def error_of_number_of_nodes(left, right, number_of_nodes_in_grid):
    n = 1000
    x_full_interval = np.linspace(left, right, num=n)


    plt.figure(4)
    plt.title("Absolute error of number of nodes in grid")
    plt.grid()
    number_of_nodes_array = []
    uniform_grid_err_array = []
    chebysh_grid_err_array = []

    for i in range(number_of_nodes_in_grid, 100, 5):
        number_of_nodes_array.append(i)
        x_uniform = np.linspace(left, right, i)
        x_chebysh = chebyshev_grid(left, right, i)
        x_interval_chebysh = np.linspace(x_chebysh[0], x_chebysh[i-1], num=n)

        spline_uniform_grid = cubic_spline(x_uniform, func)
        spline_chebysh_grid = cubic_spline(x_chebysh, func)

        # x_array_to_calculate_err = lambda x_grid: [x_grid[k] + (x_grid[k+1]-x_grid[k]/2) for k in range(len(x_grid)-1)]

        uniform_grid_err_array.append(
            max([abs(func(xi) - spline_uniform_grid(xi)) for xi in x_full_interval]))
        chebysh_grid_err_array.append(
            max([abs(func(xi) - spline_chebysh_grid(xi)) for xi in x_interval_chebysh]))
                 # if x_chebysh[0] <= xi <= x_chebysh[number_of_nodes_in_grid]]))


    plt.xlabel('number of node is grid')
    plt.ylabel('error')
    plt.yscale('log')
    plt.plot(number_of_nodes_array, uniform_grid_err_array, label='Natural cubic spline interpolation for uniform grid')
    plt.plot(number_of_nodes_array, chebysh_grid_err_array,
             label='Natural cubic spline interpolation for chebyshev grid')
    plt.legend()
    plt.grid()


def accuracy_of_grid(left, right, number_of_nodes_in_grid):
    n = 1000
    x_full_interval = np.linspace(left, right, num=n)
    plt.figure(5)
    plt.title(f"Accuracy of grid \n number of nodes in grids = {number_of_nodes_in_grid}")
    x_uniform = np.linspace(left, right, number_of_nodes_in_grid)
    x_chebyshev = chebyshev_grid(left, right, number_of_nodes_in_grid)
    spline_uniform_grid = cubic_spline(x_uniform, func)
    spline_chebysh_grid = cubic_spline(x_chebyshev, func)
    plt.plot(x_full_interval, func(x_full_interval), linewidth=0.5, label='function: x * sin(pi*x)')
    plt.plot(x_full_interval, spline_uniform_grid(x_full_interval), linewidth=1, color='yellow',
             label='Natural cubic spline on uniform grid')
    plt.plot(x_full_interval, spline_chebysh_grid(x_full_interval), linewidth=1,
             label='Natural cubic spline on chebyshev grid', color='green')
    plt.scatter(x_uniform, func(x_uniform), marker='o', linewidths=3, label='uniform grid')
    plt.scatter(x_chebyshev, func(x_chebyshev), linewidths=3, marker='o', label='chebyshev grid')
    plt.legend()


def accuracy_of_number_of_nodes_animated():
    left = -3
    right = 3
    n = 1000
    x_full_interval = np.linspace(left, right, num=n)
    fig = plt.figure()
    ax = plt.axes()
    line, = ax.plot([], [], lw=1, label='lagrange interpolation uniform grid ', color='blue')
    line2, = ax.plot([], [], lw=1, label='lagrange interpolation chebyshev grid ', color='green')
    plt.scatter(x_full_interval, func(x_full_interval), marker='*', lw=0.3, label='function', color='red')


    def init():
        line.set_data([], [])
        line2.set_data([], [])
        return line, line2,

    def animate(i):
        ax.clear()
        x = x_full_interval
        x_grid = np.linspace(left, right, i)
        # x_chebysh = chebyshev_grid(left, right, i)
        spline_uniform_grid = cubic_spline(x_grid, func)
        # spline_chebysh_grid = cubic_spline(x_chebysh, func)
        y = spline_uniform_grid(x_full_interval)
        # y_ch = spline_chebysh_grid(x_full_interval)
        line.set_data(x, y)
        # line2.set_data(x, y_ch)
        return line, line2,

    anim = ani.FuncAnimation(fig, animate, init_func=init, frames=100, interval=800, blit=True)
    plt.legend()
    plt.grid()


graph(left=-3, right=3, number_of_nodes_in_grid=15)
accuracy_of_nodes_number_uniform_grid(left=-5, right=5, number_of_nodes_in_grid=17)
accuracy_of_nodes_number_chebyshev_grid(left=-5, right=5, number_of_nodes_in_grid=17)
error_of_number_of_nodes(left=-5, right=5, number_of_nodes_in_grid=5)
accuracy_of_grid(left=0, right=10, number_of_nodes_in_grid=20)

plt.show()
