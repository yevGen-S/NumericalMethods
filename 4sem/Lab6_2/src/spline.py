import matplotlib.pyplot as plt
import numpy as np
from collections.abc import Iterable
from chebyshev_grid import chebyshev_grid
from scipy.interpolate import CubicSpline
from decimal import Decimal


def func(x):
    return x * np.sin(np.pi * x)


def g(xk, bk, ck, dk):
    def gk(x):
        return func(xk) + bk * (x - xk) + ck * ((x - xk) ** 2) + dk * ((x - xk) ** 3)

    return gk


def cubic_spline(x_grid, func):
    n = len(x_grid)
    h = [x_grid[k] - x_grid[k - 1] for k in range(1, n)]
    h.insert(0, None)
    f = lambda i, j: (func(x_grid[j]) - func(x_grid[i])) / (h[j])

    c = np.zeros(n)
    d = [None]
    b = [None]
    delta = [None, -h[2] / (2 * h[1] + h[2])]
    lambd = [None, 3 * (f(1, 2) - f(0, 1)) / (2 * (h[1] + h[2]))]

    for k in range(3, n):
        delta.append(-h[k] / (2 * h[k - 1] + 2 * h[k] + h[k - 1] * delta[k - 2]))
        lambd.append((3 * f(k - 1, k) - 3 * f(k - 2, k - 1) - h[k - 1] * lambd[k - 2])
                     / (2 * h[k - 1] + 2 * h[k] + h[k - 1] * delta[k - 2]))

    for k in range(n - 1, 1, -1):
        c[k - 1] = delta[k - 1] * c[k] + lambd[k - 1]

    a = func(x_grid)
    for k in range(1, n):
        d.append((c[k] - c[k - 1]) / (3 * h[k]))
        b.append(f(k - 1, k) + 2 / 3 * h[k] * c[k] + 1 / 3 * h[k] * c[k - 1])

    gk = [None]
    for k in range(1, n):
        gk.append(g(x_grid[k], b[k], c[k], d[k]))

    def interpolation(x):
        y = []
        if not isinstance(x, Iterable):
            x = [x]
        for value in x:
            isFound = False
            for k in range(1, n):
                if x_grid[k - 1] <= value <= x_grid[k]:
                    y.append(gk[k](value))
                    isFound = True
                    break
            if not isFound:
                y.append(None)
        return y

    return interpolation


