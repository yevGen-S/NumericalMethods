import numpy as np

n = 3
A = np.array([[3, 2, 1],
              [2, 4, 2],
              [1, 2, 5]])

b = np.array([[5, 1, 2]])
b = b.T


def LD(matrix):
    L = np.zeros((n, n))
    D = np.zeros((n, n))
    D[0][0] = A[0][0]
    for j in range(n):
        for i in range(j, n):
            sum = matrix[i][j]
            for k in range(i):
                sum = sum - L[i][k] * L[j][k] * D[k][k]
            if i == j:
                D[j][j] = sum
                L[i][j] = 1
            else:
                L[i][j] = sum / D[j][j]
    return L, D


L, D = LD(A)
print(A, '\n\n', L, '\n\n', D)
Lt = L.T
print("A = LDLt\n", L.dot(D.dot(Lt)))


def LDLt_solve():
    Z = np.zeros((n, n))
    Y = np.zeros((n, n))
    X = np.zeros((n, n))
    sum = 0
    Z = np.linalg.inv(L).dot(b)
    Y = np.linalg.inv(D).dot(Z)
    X = np.linalg.inv(Lt).dot(Y)
    return X


res = LDLt_solve()
print("Result is : \n", res)
