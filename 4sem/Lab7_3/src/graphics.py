import numpy as np
import matplotlib.pyplot as plt
from integration3_8 import integration3_8, func, integration3_8_recursive


def error_of_number_of_nodes(fun, left, right):
    plt.figure(1)
    plt.title("Error of number of nodes")
    Integral = integration3_8(fun, left, right, eps=1e-16)
    plt.plot(Integral[2], Integral[1])
    plt.yscale('log')
    plt.xscale('log')
    plt.grid()
    plt.xlabel('number of nodes')
    plt.ylabel('error')
    plt.savefig('..\\images\\error_of_number_of_nodes.png')



def number_of_nodes_of_defined_eps(fun, left, right):
    plt.figure(2)
    plt.title("Number of nodes of defined epsilon")
    eps = 1e-5
    eps_arr = []
    number_of_nodes = []
    for i in range(1, 15):
        eps_arr.append(eps)
        Integral = integration3_8(fun, left, right, eps)
        n = len(Integral[2])
        number_of_nodes.append(Integral[2][n-1])
        eps /= i

    plt.plot(eps_arr, number_of_nodes ,color='red')
    plt.grid()
    # plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('eps')
    plt.ylabel('number of nodes')
    plt.savefig('..\\images\\number_of_nodes_of_defined_eps.png')


def compare_tolerance_eps_and_exact_eps(fun, left, right):
    plt.figure(3)
    plt.title("Compare tolerance eps and exact epsilon")
    eps = 1e-5
    exact_eps_arr = []
    tolerance_eps_arr = []
    for i in range(1, 11):
        exact_eps_arr.append(eps)
        Integral = integration3_8(fun, left, right, eps)
        n = len(Integral[1])
        tolerance_eps_arr.append(Integral[1][n-1])
        eps /= i

    plt.plot(exact_eps_arr, exact_eps_arr, color='blue', label='bisectrice')
    plt.plot(tolerance_eps_arr, exact_eps_arr, label='compare')
    plt.legend()
    plt.grid()
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('eps')
    plt.ylabel('number of nodes')
    plt.savefig('..\\images\\compare_tolerance_eps_and_exact_eps.png')



error_of_number_of_nodes(func, -1, 1)
number_of_nodes_of_defined_eps(func, -1, 1)
compare_tolerance_eps_and_exact_eps(func, -1, 1)
plt.show()