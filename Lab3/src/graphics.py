import numpy as np
from matplotlib import pyplot as plt
from functions import *

cond = getMatricesWithCond()
for elem in cond:
    elem = round(elem)
iters = read_from_file2("iters_of_cond_res.txt")
print(cond)
print(iters[0])

def iters_of_cond():
    plt.figure(2)
    plt.grid()
    plt.ylabel('number of iterations')
    plt.xlabel('cond')
    plt.plot(cond, iters[0], label='eps = 1e-8', color='y')
    plt.plot(cond, iters[1], label='eps = 1e-10', color='g')
    plt.plot(cond, iters[2], label='eps = 1e-14', color='b')
    plt.legend()
    plt.title("график зависимости количесва итераций\n от числа обучсловленности | cond_step = 30")

iters_of_cond()



def iters_of_eps():
    plt.figure(100)
    plt.grid()
    plt.plot(read_file("iter_of_eps.txt")[0], read_file("iter_of_eps.txt")[1], color='r')
    plt.ylabel('number of iterations')
    plt.xscale('log')
    plt.xlabel('eps')
    plt.title("график зависимости количесва итераций\n от заданной точности")



def error_of_iter():
    plt.figure(10)
    plt.grid()
    plt.plot(read_file("error_of_iter_number.txt")[1], read_file("error_of_iter_number.txt")[0], color='g')
    plt.ylabel('abs error on current iteration')
    plt.yscale('log')
    plt.xlabel('iter')
    plt.title("График зависимости абсолютной ошибки на i-том шаге")


def iter_of_eps_of_cond():
    plt.figure(150)
    plt.grid()
    plt.plot(read_file("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results.txt")[0], read_file("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results.txt")[1], color='r',label='cond = 5')
    plt.plot(read_file("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results2.txt")[0], read_file("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results2.txt")[1], color='g',label='cond = 155')
    plt.ylabel('number of iterations')
    plt.xscale('log')
    plt.xlabel('eps')
    plt.title("график зависимости количесва итераций\n от заданной точности")
    plt.legend()

iters_of_eps()
iter_of_eps_of_cond()
error_of_iter()
plt.show()







