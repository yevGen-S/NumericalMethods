import numpy as np
import random
import math
from decimal import Decimal

eps = 1e-10
n = 10


def geom_progression(sep, left):
    arr = []
    left = 1
    for i in range(n):
        arr.append(left)
        left /= sep
    return arr


def create_rand_unsymmetric_matrix_with_defined_eigenvalues(n, left, sep):
    D = np.diag(geom_progression(sep, left))
    R = np.random.random(size=(n, n))
    A = R.dot(D).dot(np.linalg.inv(R))
    # A = A.astype(dtype = np.dtype(Decimal))
    # print(np.linalg.eigvals(A))
    return A


def create_rand_symmetric_matrix_with_defined_eigenvalues(n, left, sep):
    D = np.diag(geom_progression(sep, left))
    Q, R = np.linalg.qr(np.random.random(size=(n, n)))
    A = Q.dot(D).dot(Q.T)
    # print(np.linalg.eigvals(A))
    return A


# def create_rand_symmetric_matrix_with_defined_eigenvalues(n):
#     D = np.diag(np.linspace(1, n, n))
#     Q, R = np.linalg.qr(np.random.random(size=(n, n)))
#     A = Q.dot(D).dot(Q.T)
#     # print(np.linalg.eigvals(A))
#     return A


def outer_vector_multiply(vector1, vector2, n):
    res_matrix = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            res_matrix[i][j] += vector1[i] * vector2[j]
    return res_matrix


def to_hessenberg(A):  # householder method to get hessenberg formed matrix
    B = A
    E = np.diag(np.ones(n))
    for i in range(n - 2):
        w_m = np.zeros(shape=(n, n))
        wt = np.array(np.zeros(n))
        summa = 0

        for j in range(i + 1, n):
            summa += B[j][i] ** 2

        s = np.sign(-B[i + 1][i]) * math.sqrt(summa)

        m = 1 / math.sqrt(2 * s * (s - B[i + 1][i]))

        for k in range(n):
            if k <= i:
                wt[k] = 0

        wt[i + 1] = m * (B[i + 1][i] - s)

        for k in range(i + 2, n):
            wt[k] = m * B[k][i]

        w = wt
        H = E - 2 * outer_vector_multiply(w, wt, n)
        B = H.dot(B).dot(H)

    return B


def givens(A1):
    B = A1.copy()
    Q = np.ones(shape=(n, n))
    for j in range(n - 1):

        G = np.zeros(shape=(n, n))
        if B[j + 1][j] == 0:
            continue
        # t = Decimal( B[j][j]) / Decimal(B[j + 1][j])
        #
        # c = Decimal("1") / (Decimal.sqrt(1 + t ** 2))
        # s = Decimal(str(t)) * c

        t = B[j][j] / B[j + 1][j]

        c = 1 / (math.sqrt(1 + t ** 2))
        s = t * c

        for i in range(n):
            G[i][i] = 1

        G[j][j] = s
        G[j + 1][j + 1] = s

        G[j][j + 1] = c
        G[j + 1][j] = -c

        # print(f"G{j}\n", G)
        B = G.dot(B)
        if j == 0:
            Q = G.T
            # print("Q\n", Q)
        else:
            G1 = G.T
            # print("G1\n", G1)
            Q = Q.dot(G1)

    R = B
    return Q, R


def find_max_underdiagonal_element(matrix):
    max = 0
    for j in range(n - 1):
        for i in range(j + 1, n):
            if abs(matrix[i][j]) > max:
                max = abs(matrix[i][j])
    return max


def stop_criteria(matrix, epsilon):
    if find_max_underdiagonal_element(matrix) < epsilon:
        return True
    return False


# def qr_iteration(A):
#     for i in range(100):
#         Q, R = np.linalg.qr(A)
#         A = np.dot(R, Q)
#     return np.diag(A)


def QR(A, epsilon):
    A = to_hessenberg(A)
    counter = 0
    error_of_iter = []
    counter_mass = []
    abs_vals = np.linalg.eigvals(A)
    while not stop_criteria(A, epsilon):
        Q, R = givens(A)
        A = R.dot(Q)
        counter += 1
        counter_mass.append(counter)

        error_of_iter.append(abs(max(abs_vals) - max(np.diag(A))))
    # print("eigenvalues: ", np.diag(A))
    return np.diag(A), counter, counter_mass, error_of_iter




def QR_shift(A, epsilon):
    A = to_hessenberg(A)
    counter = 0
    error_of_iter = []
    counter_mass = []
    abs_vals = np.linalg.eigvals(A)
    while not stop_criteria(A, epsilon):
        E = np.ones(n)
        for i in range(n):
            E[i] = A[n - 1][n - 1]
        for i in range(n):
            A[i][i] -= E[i]
        Q, R = givens(A)
        A = R.dot(Q)
        for i in range(n):
            A[i][i] += E[i]
        counter += 1
        counter_mass.append(counter)

        error_of_iter.append(np.linalg.norm(np.sort(abs_vals) - np.sort(np.diag(A))))
    # print("eigenvalues: ", np.diag(A))
    return np.diag(A), counter, counter_mass, error_of_iter


# a = create_rand_unsymmetric_matrix_with_defined_eigenvalues(n, 1, 0.5)
# print(a)
# QR_shift(a, epsilon=eps)
