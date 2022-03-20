import matplotlib.pyplot as plt
import numpy as np


def f(x, y, z):  # y`` = z` = np.sqrt(x) - 2 * y - (2 - x) * z) / (2 * x * (x + 2)
    return (np.sqrt(x) - 2 * y - (2 - x) * z) / (2 * x * (x + 2))


def g(x, y, z):  # y` = z
    return z


def runge_kutta_4order(x0, y0, z0, x_res, h, eps):
    def runge_kutta_body(x0, y0, z0, x_res, h):

        n = int((x_res - x0) / h)
        z_arr = []
        y_arr = []
        x_arr = []

        for i in range(n + 1):
            z_arr.append(z0)
            y_arr.append(y0)
            x_arr.append(x0)

            k1 = h * f(x0, y0, z0)
            q1 = h * g(x0, y0, z0)

            k2 = h * f(x0 + 0.5 * h, y0 + 0.5 * q1, z0 + 0.5 * k1)
            q2 = h * g(x0 + 0.5 * h, y0 + 0.5 * q1, z0 + 0.5 * k1)

            k3 = h * f(x0 + 0.5 * h, y0 + 0.5 * q2, z0 + 0.5 * k2)
            q3 = h * g(x0 + 0.5 * h, y0 + 0.5 * q2, z0 + 0.5 * k2)

            k4 = h * f(x0 + h, y0 + q3, z0 + k3)
            q4 = h * g(x0 + h, y0 + q3, z0 + k3)

            yi = y0 + (q1 + 2.0 * q2 + 2.0 * q3 + q4) / 6.0
            zi = z0 + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0

            z0 = zi
            y0 = yi

            x0 = x0 + h

        return x_arr, y_arr, z_arr

    max_error = lambda y_arr1, y_arr2: max([abs(y_arr1[i - 1] - y_arr2[2 * i - 2]) for i in range(1, len(y_arr1)+1)])

    iter = 1
    runge_res1 = runge_kutta_body(x0, y0, z0, x_res, h)
    h = h / 2
    runge_res2 = runge_kutta_body(x0, y0, z0, x_res, h)
    error_arr = []
    iter_arr = []
    iter_arr.append(iter)
    iter += 1
    error_arr.append(max_error(runge_res1[1], runge_res2[1]))

    while (max_error(runge_res1[1], runge_res2[1]) / (2 ** 4 + 1)) > eps:
        runge_res1 = runge_res2
        h = h / 2
        runge_res2 = runge_kutta_body(x0, y0, z0, x_res, h)
        error_arr.append(max_error(runge_res1[1], runge_res2[1]))
        iter_arr.append(iter)
        iter += 1
    return runge_res2, error_arr, iter_arr, h



