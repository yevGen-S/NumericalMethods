import numpy as np
import random


def create_rand_symetric_matrix_with_defined_cond(n, cond):
    log_cond = np.log(cond)
    exp_vec = np.arange(-log_cond/4., log_cond * (n + 1)/(4 * (n - 1)), log_cond/(2.*(n-1)))
    s = np.exp(exp_vec)
    S = np.diag(s)
    U, _ = np.linalg.qr((np.random.rand(n, n) - 5.) * 200)
    V, _ = np.linalg.qr((np.random.rand(n, n) - 5.) * 200)
    A = U.dot(S).dot(V.T)
    A = A.dot(A.T)
    A = (A + A.T)/2
    return A

def create_rand_matrix_with_defined_cond(n, cond):
    log_cond = np.log(cond)
    exp_vec = np.arange(-log_cond/4., log_cond * (n + 1)/(4 * (n - 1)), log_cond/(2.*(n-1)))
    s = np.exp(exp_vec)
    S = np.diag(s)
    U, _ = np.linalg.qr((np.random.rand(n, n) - 5.) * 200)
    V, _ = np.linalg.qr((np.random.rand(n, n) - 5.) * 200)
    A = U.dot(S).dot(V.T)
    A = A.dot(A.T)
    return A

# print(create_rand_symetric_matrix_with_defined_cond(5,100))