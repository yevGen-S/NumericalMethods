import numpy as np
from matplotlib import pyplot as plt
import functions

x_ex = np.ones(10)


def create_Ab():
    list_of_A = []
    list_of_b = []
    cond = 10
    for i in range(16):
        A = functions.create_rand_symetric_matrix_with_defined_cond(10, cond)
        list_of_A.append(A)
        b = A.dot(x_ex)
        list_of_b.append(b)
        cond *= 10

    return list_of_A, list_of_b


# Creating random  A matrices with cond from 10 till 10**16 and b vectors
A, b = create_Ab()

# writing to files matrices for using method
functions.write_to_file_matrix(A, "A.csv")
functions.write_to_file_matrix(b, "b.csv")

# reading results of using method from file
x = functions.read_from_file("X1.csv")


def graph_err_of_cond():
    x_rel_error = []
    cond = []

    for i in range(16):
        x_rel_error.append(np.linalg.norm(x[i] - x_ex) / np.linalg.norm(x_ex))
        print(np.linalg.norm(x[i] - x_ex))
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


def data_for_2_graph():
    list_of_b2 = []
    A2 = functions.create_rand_symmetric_matrix_with_defined_cond(10, 100)
    b2 = A2.dot(x_ex)
    list_of_b2.append(b2)

    for i in range(16):
        b2 = b2 + 0.001
        list_of_b2.append(b2)

    functions.write_to_file_matrix(A2, "A2.csv")
    functions.write_to_file_matrix(list_of_b2, "b2.csv")

    return list_of_b2


b2 = data_for_2_graph()[0]
list_of_b2 = data_for_2_graph()


def graph_err_of_b_changing():
    x_rel_error2 = []
    err_db = []

    for i in range(16):
        x_rel_error2.append(np.linalg.norm(x[i] - x_ex) / np.linalg.norm(x_ex))

    for i in range(16):
        err_db.append(np.linalg.norm(b2 - list_of_b2[i]) / np.linalg.norm(b2))

    plt.figure(2)
    plt.grid()
    plt.ylabel('||X-X_ex|| / ||X_ex||')
    plt.xlabel('||db|| / ||b||')
    plt.yscale('log')
    # plt.xscale('log')
    plt.title("Error X of changing b ")
    plt.plot(err_db, x_rel_error2)



graph_err_of_b_changing()
plt.show()