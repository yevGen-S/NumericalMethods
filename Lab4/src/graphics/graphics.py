import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from qr import create_rand_unsymmetric_matrix_with_defined_eigenvalues, create_rand_symmetric_matrix_with_defined_eigenvalues ,QR
n = 10
eps1 = 1e-10
eps2 = 1e-5

def get_data_for_iters_of_separability():
    iters = []
    separability = []
    val = 1.1
    for i in range(10):
        A = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n,val)
        separability.append(1 / val)
        iters.append(QR(A, eps1)[1])
        val += 0.1
        print(i)
    return separability, iters

data1 = get_data_for_iters_of_separability()


def get_data_of_error_of_iter():
    error = []
    iter = []
    val1 = 1.2
    val2 = 1.8

    A = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n, val1)
    A1 = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n, val2)
    res1 = QR(A, eps1)
    res2 = QR(A1, eps1)
    return res1, res2


def graph_error_of_iter():
    data2 = get_data_of_error_of_iter()
    plt.figure(12)
    plt.title("График зависимости точности от итерации")
    plt.ylabel('error')
    plt.xlabel('iter')
    plt.plot(data2[0][2], data2[0][3], label='QR separability 1/1.2')
    plt.plot(data2[1][2],data2[1][3], label='QR separability 1/1.8')
    plt.grid()
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()

# graph_error_of_iter()







def graph_iter_of_sep():
    plt.figure(1)
    plt.title("График зависимости времени выполнения от отделимости")
    plt.ylabel('iters')
    plt.xlabel('separability')
    plt.plot(data1[0], data1[1], label='QR 1')

    plt.grid()
    # plt.xscale('log')
    # plt.yscale('log')
    plt.legend()



def iters_of_eps():
    iters = []
    mass_eps = []
    eps = 1e-10
    for i in range(5):
        A = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n,1.1)
        iters.append(QR(A,eps)[1])
        mass_eps.append(eps)
        eps*=10

    plt.figure(122)
    plt.title("График количества итераций от заданной точности")
    plt.ylabel('iters')
    plt.xlabel('eps')
    plt.plot(mass_eps, iters, label='QR ')

    plt.grid()
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()


iters_of_eps()
# graph_iter_of_sep()



plt.show()
