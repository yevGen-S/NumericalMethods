import numpy as np
from matplotlib import pyplot as plt
from functions import *
from scipy.optimize import curve_fit


# cond = getMatricesWithCond()
# for elem in cond:
#     elem = round(elem)
# iters = read_from_file2("iters_of_cond_res.txt")
# print(cond)
# print(iters[0])

# def iters_of_cond():
#     plt.figure(2)
#     plt.grid()
#     plt.ylabel('number of iterations')
#     plt.xlabel('cond')
#     plt.plot(cond, iters[0], label='eps = 1e-8', color='y')
#     plt.plot(cond, iters[1], label='eps = 1e-10', color='g')
#     plt.plot(cond, iters[2], label='eps = 1e-14', color='b')
#     plt.legend()
#     plt.title("график зависимости количесва итераций\n от числа обучсловленности | cond_step = 30")
#
# iters_of_cond()
#
#
#
# def iters_of_eps():
#     plt.figure(100)
#     plt.grid()
#     plt.plot(read_file("iter_of_eps.txt")[0], read_file("iter_of_eps.txt")[1], color='r')
#     plt.ylabel('number of iterations')
#     plt.xscale('log')
#     plt.xlabel('eps')
#     plt.title("график зависимости количесва итераций\n от заданной точности")
#
#
#
# def error_of_iter():
#     plt.figure(10)
#     plt.grid()
#     plt.plot(read_file("error_of_iter_number.txt")[1], read_file("error_of_iter_number.txt")[0], color='g')
#     plt.ylabel('abs error on current iteration')
#     plt.yscale('log')
#     plt.xlabel('iter')
#     plt.title("График зависимости абсолютной ошибки на i-том шаге")
#
#
# def iter_of_eps_of_cond():
#     plt.figure(150)
#     plt.grid()
#     plt.plot(read_file("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results.txt")[0], read_file("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results.txt")[1], color='r',label='cond = 5')
#     plt.plot(read_file("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results2.txt")[0], read_file("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results2.txt")[1], color='g',label='cond = 155')
#     plt.ylabel('number of iterations')
#     plt.xscale('log')
#     plt.xlabel('eps')
#     plt.title("график зависимости количесва итераций\n от заданной точности")
#     plt.legend()


# iters_of_eps()
# iter_of_eps_of_cond()
# error_of_iter()


def graph_time_of_rang():
    rang = [i for i in range(2, 1000)]
    print(rang)
    time_iter = read_from_file2("time_of_rang_iter.txt")[0][:-1]
    time_direct = read_from_file2("time_of_rang_direct.txt")[0][:-1]
    print(len(rang))
    plt.figure(11)
    plt.title("График зависимости времени выполнения от ранга матрицы")
    plt.ylabel('time')
    plt.xlabel('rang')
    plt.plot(rang, time_iter, label='fpi')
    plt.plot(rang, time_direct, label='LDLt')
    plt.grid()
    plt.xscale('log')
    plt.yscale('log')

    plt.legend()


def graph_time_of_rang2():
    rang = [i for i in range(2, 1000)]
    print(rang)
    time_iter = read_from_file2("time_of_rang_iter.txt")[0][:-1]
    time_direct = read_from_file2("time_of_rang_direct.txt")[0][:-1]
    print(len(rang))
    plt.figure(10)
    plt.title("График зависимости времени выполнения от ранга матрицы")
    plt.ylabel('time')
    plt.xlabel('rang')
    plt.plot(rang, time_iter, label='fpi')
    plt.plot(rang, time_direct, label='LDLt')
    plt.grid()

    plt.legend()


def fun_cube(x, b):
    return x ** 3 / b


def graph_time_of_rang3():
    rang = [i for i in range(1000, 2000, 50)]



    # time_iter = read_from_file2("time_of_rang_iter2.txt")[0][:-1]
    time_direct = read_from_file2("time_of_rang_direct2.txt")[0][:-1]
    print(len(rang))
    plt.figure(12)
    plt.title("График зависимости времени выполнения от ранга матрицы")
    plt.ylabel('time')
    plt.xlabel('rang , step = 50')
    # plt.plot(rang, time_iter, label='fpi')
    plt.plot(rang, time_direct, 'o', label='LDLt')


    param, res1 = curve_fit(fun_cube, rang, time_direct)
    print("approx coefficients: ", param)
    ans = [fun_cube(i, param[0]) for i in rang]
    plt.plot(rang, ans, label='y = x^3/a, approximation', color='r')

    # plt.xscale('log')
    # plt.yscale('log')
    plt.grid()

    plt.legend()



def graph_time_of_rang4():
    rang = [i for i in range(2, 1000)]

    time_direct = read_from_file2("time_of_rang_direct.txt")[0][:-1]

    plt.figure(15)
    plt.title("График зависимости времени выполнения от ранга матрицы")
    plt.ylabel('time')
    plt.xlabel('rang')
    plt.plot(rang, time_direct, label='LDLt')

    param, res1 = curve_fit(fun_cube, rang, time_direct)
    print("approx coefficients: ", param)
    ans = [fun_cube(i, param[0]) for i in rang]
    plt.plot(rang, ans, label='y = x^3/a, approximation', color='r')

    plt.grid()
    plt.legend()


# graph_time_of_rang()
# graph_time_of_rang2()
graph_time_of_rang3()
graph_time_of_rang4()

plt.show()
