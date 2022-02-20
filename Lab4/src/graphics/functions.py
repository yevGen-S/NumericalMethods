import numpy as np
import csv
import random
N = 10



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




def read_file(name_of_file):
    Y, X = np.loadtxt(name_of_file, delimiter=';', unpack=True)
    return Y, X




def create_rand_matrix_with_defined_cond(n, cond):
    D = np.diag(np.ones(n))
    D[n - 1][n - 1] = cond
    Q, R = np.linalg.qr(np.random.random(size=(n, n)))
    A = Q.dot(D).dot(Q.T)
    A = (A + A.T) / 2
    print(np.linalg.cond(A))
    return A


# def create_rand_unsymmetric_matrix_with_defined_eigenvalues(n):
#     D = np.diag(np.linspace(1, n, n))
#     R = np.random.random(size=(n, n))
#     A = R.dot(D).dot(np.linalg.inv(R))
#     # print(np.linalg.eigvals(A))
#     return A

# def create_rand_symmetric_matrix_with_defined_eigenvalues(n):
#     D = np.diag(np.linspace(1, n, n))
#     Q , R = np.linalg.qr( np.random.random(size=(n, n)))
#     A = Q.dot(D).dot(Q.T)
#     # print(np.linalg.eigvals(A))
#     return A

def geom_progression(val):
    arr = []
    left = 1
    for i in range(N):
        arr.append(left)
        left *= val
    return arr

def create_rand_symmetric_matrix_with_defined_eigenvalues(n,val):
    D = np.diag(geom_progression(val))
    Q , R = np.linalg.qr( np.random.random(size=(n, n)))
    A = Q.dot(D).dot(Q.T)
    print(np.diag(D))
    return A

def create_rand_unsymmetric_matrix_with_defined_eigenvalues(n,val):
    D = np.diag(geom_progression(val))
    print(D)
    R = np.random.random(size=(n, n))
    A = R.dot(D).dot(np.linalg.inv(R))
    # A = A.astype(dtype = np.dtype(Decimal))
    # print(np.linalg.eigvals(A))
    return A

a = create_rand_symmetric_matrix_with_defined_eigenvalues(N,1.1)
# print(a)
write_matrix(a, "matrix.csv")