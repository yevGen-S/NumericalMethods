import numpy as np

n = 3
A = ([[3, 2, 1],
     [2, 4, 2],
     [1, 2, 5]])


def LD(matrix):
    L = np.zeros((n, n))
    D = np.zeros((n, n))
    D[0][0] = A[0][0]
    for j in range(n):
        for i in range(j,n):
            sum = matrix[i][j]
            for k in range(i):
                sum = sum - L[i][k] * L[j][k] * D[k][k]
            if i == j:
                D[j][j] = sum
                L[i][j] = 1
            else:
                L[i][j] = sum / D[j][j]
    return L, D


L,D = LD(A)
print(A, '\n\n', L, '\n\n', D)
Lt = L.T
print("A = LDLt\n", L.dot(D.dot(Lt)))