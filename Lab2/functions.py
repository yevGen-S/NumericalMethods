import numpy as np
import csv
import random


N = 10


# def create_rand_symmetric_matrix_with_defined_cond(n, cond):
#     log_cond = np.log(cond)
#     exp_vec = np.arange(-log_cond / 4., log_cond * (n + 1) / (4 * (n - 1)), log_cond / (2. * (n - 1)))
#     s = np.exp(exp_vec)
#     S = np.diag(s)
#     U, _ = np.linalg.qr((np.random.rand(n, n) - 5.) * 200)
#     V, _ = np.linalg.qr((np.random.rand(n, n) - 5.) * 200)
#     A = U.dot(S).dot(V.T)
#     A = A.dot(A.T)
#     A = (A + A.T) / 2
#     print(np.linalg.cond(A)-cond)
#     return A

# def create_rand_matrix_with_defined_cond(n, cond):
#     log_cond = np.log(cond)
#     exp_vec = np.arange(-log_cond / 4., log_cond * (n + 1) / (4 * (n - 1)), log_cond / (2. * (n - 1)))
#     s = np.exp(exp_vec)
#     S = np.diag(s)
#     U, _ = np.linalg.qr((np.random.rand(n, n) - 5.) * 200)
#     V, _ = np.linalg.qr((np.random.rand(n, n) - 5.) * 200)
#     A = U.dot(S).dot(V.T)
#     A = A.dot(A.T)
#     return A


def create_rand_symmetric_matrix_with_defined_cond(n, cond):
    D = np.diag(np.ones(n))
    D[n - 1][n - 1] = cond
    Q, R = np.linalg.qr(np.random.random(size=(n, n)))
    A = Q.dot(D).dot(Q.T)
    A = (A + A.T) / 2
    print(np.linalg.cond(A))
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
        for i in range(16):
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
