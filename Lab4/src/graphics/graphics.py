import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from qr import create_rand_unsymmetric_matrix_with_defined_eigenvalues, \
    create_rand_symmetric_matrix_with_defined_eigenvalues, QR,QR_shift

n = 10
eps1 = 1e-10
eps2 = 1e-5


def get_data_for_iters_of_separability():
    iters = []
    iters2 = []
    separability = []
    sep = 0.1
    for i in range(8):
        A = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n, 1, sep)
        A2 = np.copy(A)
        separability.append(sep)
        iters.append(QR(A, eps1)[1])
        iters2.append(QR_shift(A2,eps1)[1])
        sep += 0.1
    return separability, iters, iters2


def get_data_of_error_of_iter(sep1, sep2):
    A = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n, 1, sep1)
    A1 = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n, 1, sep2)
    A2 = np.copy(A)
    A3 = np.copy(A1)
    res1 = QR(A, eps1)
    res2 = QR(A1, eps1)
    res3 = QR_shift(A2,eps1)
    res4 = QR_shift(A3,eps1)
    return res1, res2, res3, res4


def graph_error_of_iter():
    sep1 = 0.5
    sep2 = 0.9
    data2 = get_data_of_error_of_iter(sep1, sep2)
    plt.figure(12)
    plt.title("График зависимости точности от итерации eps=1e-10")
    plt.ylabel('error')
    plt.xlabel('iter')
    plt.plot(data2[0][2], data2[0][3], label=f'QR separability {sep1}')
    plt.plot(data2[1][2], data2[1][3], label=f'QR separability {sep2}')
    plt.grid()
    # plt.xscale('log')
    plt.yscale('log')
    plt.legend()

# def graph_error_of_iter():
#     sep1 =1.2
#     sep2 = 1.01
#     data2 = get_data_of_error_of_iter(sep1, sep2)
#     plt.figure(12)
#     plt.title("График зависимости точности от итерации")
#     plt.ylabel('error')
#     plt.xlabel('iter')
#     plt.plot(data2[0][2], data2[0][3], label=f'QR separability 1/{val1}')
#     plt.plot(data2[1][2], data2[1][3], label=f'QR separability 1/{val2}')
#     plt.grid()
#     plt.xscale('log')
#     plt.yscale('log')
#     plt.legend()


graph_error_of_iter()


def graph_iter_of_sep():
    data1 = get_data_for_iters_of_separability()
    plt.figure(1)
    plt.title("График зависимости количества итераций от отделимости")
    plt.ylabel('iters')
    plt.xlabel('separability')
    plt.plot(data1[0], data1[1], label='QR')
    plt.plot(data1[0],data1[2], label='QR with shift')
    plt.grid()
    # plt.xscale('log')
    # plt.yscale('log')
    plt.legend()


def iters_of_eps():
    iters1 = []
    iters2=[]
    mass_eps = []
    eps = 1e-14
    sep = 0.99
    for i in range(10):
        A = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n, 1, sep)
        A2 = np.copy(A)
        iters1.append(QR(A, eps)[1])
        iters2.append(QR_shift(A2, eps)[1])
        mass_eps.append(eps)
        eps *= 10

    plt.figure(122)
    plt.title(f"График количества итераций от заданной точности\n с числом отделимости={sep}")
    plt.ylabel('iters')
    plt.xlabel('eps')
    plt.plot(mass_eps, iters1,'-*', label='QR ')
    plt.plot(mass_eps, iters2, label='QR_shift ')

    plt.grid()
    plt.xscale('log')
    # plt.yscale('log')
    plt.legend()


iters_of_eps()
graph_iter_of_sep()

plt.show()
