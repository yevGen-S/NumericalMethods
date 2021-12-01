import numpy as np
import csv
import random

N = 10


def create_rand_matrix_with_diag_dominance(n, cond):
    D = np.diag(np.ones(n))
    D[n - 1][n - 1] = cond
    Q, R = np.linalg.qr(np.random.random(size=(n, n)))
    A = Q.dot(D).dot(Q.T)
    for i in range(n):
        for j in range(n):
            A[i][i] += abs(A[i][j])
    # A = (A + A.T) / 2
    # print(np.linalg.cond(A))
    return A


def create_rand_x_ex():
    x_ex = []
    for i in range(10):
        x_ex.append(random.random())
    return x_ex


def write_to_file_matrix(list_of_matrices, name_of_file):
    with open(name_of_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if name_of_file == "A2.csv":
            for row in range(10):
                writer.writerow(list_of_matrices[row])
            return 0
        for i in range(15):
            matrix = list_of_matrices[i]
            if name_of_file == "b.csv" or name_of_file == "b2.csv":  # if it's vector
                writer.writerow(matrix)
                writer.writerow('\t')
                continue
            for row in matrix:
                writer.writerow(row)
            writer.writerow('\t')

    return 0


def read_from_file(name_of_file):
    array = []
    with open(name_of_file, "r") as file:
        reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            array.append(row)
        for i in range(16):
            array[i] = array[i][:-1]
        x = np.array(array)

    return x


def read_from_file2(name_of_file):
    array = []
    with open(name_of_file, "r") as file:
        reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            array.append(row)
    return array


def write_matrix(matrix, name_of_file):
    with open(name_of_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in matrix:
            writer.writerow(row)


print("\n\n")


def getMatricesWithCond():
    counter = 0
    need_cond = 5
    list_of_conds = []
    list_of_matrixes = []
    while True:
        A = create_rand_matrix_with_diag_dominance(10, need_cond)
        if (np.linalg.cond(A) > (need_cond - 1)) and (np.linalg.cond(A) < (need_cond + 1)):
            list_of_conds.append(np.linalg.cond(A))
            list_of_matrixes.append(A)
            need_cond += 30
            counter += 1
            if (counter == 15):
                break
        # print(np.linalg.cond(A))
    print(list_of_conds)
    write_to_file_matrix(list_of_matrixes, "D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\src\\iters_of_cond.csv")
    return list_of_conds




def read_file(name_of_file):
    Y, X = np.loadtxt(name_of_file, delimiter=';', unpack=True)
    return Y, X