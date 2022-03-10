from integration_gauss_5nodes import integration_gauss_5nodes
from integration3_8 import integration3_8, func
from matplotlib import pyplot as plt
import numpy as np


def error_of_number_of_nodes(fun, left, right):
    plt.figure(1)
    plt.title(f"Error of number of sections \n interval = [{left, right}]")
    Integral_gauss = integration_gauss_5nodes(fun, left, right, 1024, 1e-15)
    Integral_3_8 = integration3_8(fun, left, right, 1e-15)
    plt.plot(Integral_gauss[2], Integral_gauss[1], label='Gauss method 5 nodes')
    plt.plot(Integral_3_8[2], Integral_3_8[1], label='3/8 method')
    plt.legend()
    plt.yscale('log')
    # plt.xscale('log')
    plt.grid()
    plt.xlabel('number of sections')
    plt.ylabel('error')
    plt.savefig(f'..\\images_compare\\compare_error_of_number_of_sections_[{left, right}].png')


def number_of_nodes_of_defined_eps(fun, left, right):
    plt.figure(2)
    plt.title(f"Number of nodes of defined epsilon \n interval = [{left, right}]")
    eps = 1e-5
    eps_arr = []
    number_of_nodes_gauss = []
    number_of_nodes_3_8 = []

    for i in range(1, 11):
        eps_arr.append(eps)
        Integral_gauss = integration_gauss_5nodes(fun, left, right, 1024, eps)
        n = len(Integral_gauss[2])
        number_of_nodes_gauss.append(Integral_gauss[2][n - 1])
        Integral_3_8 = integration3_8(fun, left, right, eps)
        n = len(Integral_3_8[2])
        number_of_nodes_3_8.append(Integral_3_8[2][n - 1])
        eps /= 10

    plt.plot(eps_arr, number_of_nodes_gauss, label='Gauss 5 nodes')
    plt.plot(eps_arr, number_of_nodes_3_8, label='3/8')
    plt.legend()
    plt.grid()
    # plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('eps')
    plt.ylabel('number of sections')
    plt.savefig(f'..\\images_compare\\compare_number_of_sections_of_defined_eps_[{left, right}].png')


def compare_tolerance_eps_and_exact_eps(fun, left, right):
    plt.figure(3)
    plt.title(f"Compare tolerance eps and exact epsilon of Gauss method and 3/8 \n interval = [{left, right}]")
    eps = 1e-5
    exact_eps_arr = []
    tolerance_eps_arr_gauss = []
    tolerance_eps_arr_3_8 = []

    for i in range(1, 11):
        exact_eps_arr.append(eps)
        Integral_gauss = integration_gauss_5nodes(fun, left, right, 1024, eps)
        n = len(Integral_gauss[1])
        tolerance_eps_arr_gauss.append(Integral_gauss[1][n - 1])
        Integral_3_8 = integration3_8(fun, left, right, eps)
        n = len(Integral_3_8[1])
        tolerance_eps_arr_3_8.append(Integral_3_8[1][n - 1])
        eps /= 10

    plt.plot(exact_eps_arr, exact_eps_arr, color='blue', label='bisectrice')
    plt.plot(exact_eps_arr, tolerance_eps_arr_gauss, label='Gauss compare')
    plt.plot(exact_eps_arr, tolerance_eps_arr_3_8, label='3/8 compare')

    plt.legend()
    plt.grid()
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('eps')
    plt.ylabel('number of sections')
    plt.savefig(f'..\\images_compare\\compare_tolerance_eps_and_exact_eps_[{left, right}].png')


# def order_of_convergence(fun, left, right):
#     plt.figure(4)
#     plt.title(f"Identify an order of convergence of Gauss method and 3/8. \n interval = [{left, right}]")
#     eps = 1e-15
#     Integral_gauss = integration_gauss_5nodes(fun, left, right, 1024, eps)
#     Integral_3_8 = integration3_8(fun, left, right, eps)
#     p_gauss = []
#     i_arr_gauss = []
#     p_3_8 = []
#     i_arr_3_8 = []
#
#     for i in range(1, len(Integral_gauss[2])):
#         p_gauss.append(np.log2(Integral_gauss[1][i - 1] / Integral_gauss[1][i]))
#         i_arr_gauss.append(i)
#
#     for i in range(1, len(Integral_3_8[2])):
#         p_3_8.append(np.log2(Integral_3_8[1][i - 1] / Integral_3_8[1][i]))
#         i_arr_3_8.append(i)
#
#     plt.grid()
#     plt.plot(i_arr_gauss, p_gauss, label='p of convergence Gauss')
#     plt.plot(i_arr_3_8, p_3_8, label='p of convergence 3/8')
#     plt.legend()
#     plt.xlabel('iteration')
#     plt.ylabel('p')
#     plt.savefig(f'..\\images_compare\\compare_order_of_convergence_[{left, right}].png')


def my_func_graphic(left, right):
    plt.figure(100)
    x = np.linspace(left, right, 1000)
    y = func(x)
    plt.plot(x, y, label='my func')
    plt.legend()


my_func_graphic(-10, 10)
error_of_number_of_nodes(func, -1, 1)
number_of_nodes_of_defined_eps(func, -1, 1)
compare_tolerance_eps_and_exact_eps(func, -1, 1)


# error_of_number_of_nodes(func, 6, 8)
# number_of_nodes_of_defined_eps(func, 6, 8)
# compare_tolerance_eps_and_exact_eps(func, 6, 8)
plt.show()
