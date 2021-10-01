import numpy as np

M1 = 2.135
M2 = -35


def fun_trans(x):
    return (x - 1) ** 2 - np.exp(-x)


def fun_poly(x):
    return x ** 4 - 10 * x ** 2 - 16 * x + 5


def fun_trans_d(x):
    return 2 * (x - 1) + np.exp(-x)


def fun_poly_d(x):
    return 4 * x ** 3 - 20 * x - 16


def phi_fun_trans(x):
    return (np.exp(-x) - 1) / x + 2


# def phi_fun_trans(x):
#     return x - (2.0 / M1) * ((x - 1.0) * (x - 1.0) - np.exp(-x))


def phi_fun_trans_d(x):
    return -np.exp(-x) / x - (np.exp(-x) - 1) / (x ** 2)


# def phi_fun_trans_d(x):
#      return 1 - (2.0 / M1) * (2 * (x - 1.0) + np.exp(-x))


# def phi_fun_poly(x):
#     return (x ** 4 - 10 ** 2 + 5) / 16

def phi_fun_poly(x):
    return x - (2 / M2) * (x ** 4 - 10 * x ** 2 - 16 * x + 5)


# def phi_fun_poly_d(x):
#     return (4 ** 3 - 20 * x) / 16


def phi_fun_poly_d(x):
    return 1 - (2 / M2) * (4 * x ** 3 - 20 * x - 16)


def read_file():
    Y, X = np.loadtxt("iter_from_eps.txt", delimiter=' ', unpack=True)
    return Y, X
