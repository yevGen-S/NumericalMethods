import numpy as np
from matplotlib import pyplot as plt
import functions
from data_getting import x_ex, x, x2, list_of_b2


def graph_err_of_cond():
    x_rel_error = []
    cond = []

    for i in range(16):
        x_rel_error.append(np.linalg.norm(x[i] - x_ex) / np.linalg.norm(x_ex))
        cond.append(10 ** (i + 1))
    plt.figure(1)
    plt.grid()
    plt.ylabel('||X-X_ex|| / ||X_ex||')
    plt.xlabel('cond')
    plt.yscale('log')
    plt.xscale('log')
    plt.plot(cond, x_rel_error)
    plt.title("Error of cond number")


# График зависимости относительной погрешности решений от числа обусловленности
graph_err_of_cond()


def graph_err_of_b_changing():
    x_rel_error2 = []
    err_db = []

    for i in range(16):
        x_rel_error2.append(np.linalg.norm(x2[i] - x_ex) / np.linalg.norm(x_ex))

    for i in range(16):
        err_db.append(np.linalg.norm(list_of_b2[0] - list_of_b2[i]) / np.linalg.norm(list_of_b2[0]))

    plt.figure(2)
    plt.grid()
    plt.ylabel('||X-X_ex|| / ||X_ex||')
    plt.xlabel('||db|| / ||b||')
    # plt.yscale('log')
    # plt.xscale('log')
    plt.title("Error X of changing b ")
    plt.plot(err_db, x_rel_error2, color='red')


# График зависимости отн погрешности решений от относительнйо погрешности возмущений вектора свободных членов
graph_err_of_b_changing()
plt.show()
