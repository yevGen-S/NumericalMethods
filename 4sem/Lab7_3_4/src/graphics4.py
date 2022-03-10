import numpy as np
import matplotlib.pyplot as plt
from integration_gauss_5nodes import extra_work as ex_w, integration_gauss_5nodes, func
from scipy.integrate import quad

a = 0  # left border
b = 1  # right border


# -----------------------------------------------Gauss-method-with-5-nodes-----------------------------------------------------------


def error_of_number_of_nodes(fun, left, right):
    plt.figure(1)
    plt.title(f"Error of number of sections \n interval = [{left, right}]")
    Integral = integration_gauss_5nodes(fun, left, right, 1024, 1e-15)
    print("error of number of sections", Integral)
    plt.plot(Integral[2], Integral[1])
    plt.yscale('log')
    # plt.xscale('log')
    plt.grid()
    plt.xlabel('number of sections')
    plt.ylabel('error')
    plt.savefig(f'..\\images_gauss_5\\gauss_error_of_number_of_sections_[{left, right}].png')


def number_of_nodes_of_defined_eps(fun, left, right):
    plt.figure(2)
    plt.title(f"Number of nodes of defined epsilon \n interval = [{left, right}]")
    eps = 1e-5
    eps_arr = []
    number_of_nodes = []
    for i in range(1, 11):
        eps_arr.append(eps)
        Integral = integration_gauss_5nodes(fun, left, right, 1024, eps)
        n = len(Integral[2])
        number_of_nodes.append(Integral[2][n - 1])
        eps /= 10

    plt.plot(eps_arr, number_of_nodes, color='red')
    print("number of sections of defined eps", eps_arr, number_of_nodes)
    plt.grid()
    # plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('eps')
    plt.ylabel('number of sections')
    plt.savefig(f'..\\images_gauss_5\\gauss_number_of_sections_of_defined_eps_[{left, right}].png')


def compare_tolerance_eps_and_exact_eps(fun, left, right):
    plt.figure(3)
    plt.title(f"Compare tolerance eps and exact epsilon of Gauss method with 5 nodes \n interval = [{left, right}]")
    eps = 1e-5
    exact_eps_arr = []
    tolerance_eps_arr = []
    for i in range(1, 11):
        exact_eps_arr.append(eps)
        Integral = integration_gauss_5nodes(fun, left, right, 1024, eps)
        n = len(Integral[1])
        tolerance_eps_arr.append(Integral[1][n - 1])
        eps /= 10

    plt.plot(exact_eps_arr, exact_eps_arr, color='blue', label='bisectrice')
    plt.plot(exact_eps_arr, tolerance_eps_arr, label='compare')
    print("compare_tolerance_eps_and_exact_eps", exact_eps_arr, tolerance_eps_arr)
    plt.legend()
    plt.grid()
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('eps')
    plt.ylabel('number of sections')
    plt.savefig(f'..\\images_gauss_5\\gauss_compare_tolerance_eps_and_exact_eps_[{left, right}].png')


def order_of_convergence(fun, left, right):
    plt.figure(4)
    plt.title(f"Identify an order of convergence of Gauss method with 5 nodes. \n interval = [{left, right}]")
    eps = 1e-15
    Integral = integration_gauss_5nodes(fun, left, right, 1024, eps)
    p = []
    i_arr = []
    for i in range(1, len(Integral[2])):
        p.append(np.log2(Integral[1][i - 1] / Integral[1][i]))
        i_arr.append(i)
    print(Integral)
    plt.grid()
    plt.plot(i_arr, p)
    plt.xlabel('iteration')
    plt.ylabel('p')
    plt.savefig(f'..\\images_gauss_5\\gauss_order_of_convergence_[{left, right}].png')


def my_func_graphic(left, right):
    plt.figure(100)
    x = np.linspace(left, right, 1000)
    y = func(x)
    plt.plot(x, y, label='my func')
    plt.legend()


# my_func_graphic(-10, 10)
# error_of_number_of_nodes(func, -1, 1)
# number_of_nodes_of_defined_eps(func, -1, 1)
# compare_tolerance_eps_and_exact_eps(func, -1, 1)
# order_of_convergence(func, -1, 1)
#
error_of_number_of_nodes(func, 6, 8)
number_of_nodes_of_defined_eps(func, 6, 8)
compare_tolerance_eps_and_exact_eps(func, 6, 8)
order_of_convergence(func, 6, 8)
plt.show()
