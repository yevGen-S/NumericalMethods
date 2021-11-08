import numpy as np
from matplotlib import pyplot as plt
import functions

x_ex = np.ones(10)


def create_Ab():
    list_of_A = []
    list_of_b = []
    cond = 10
    for i in range(16):
        A = functions.create_rand_symmetric_matrix_with_defined_cond(10, cond)
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
x2 = functions.read_from_file("X2.csv")


def data_for_2_graph():
    list_of_b2 = []
    A2 = functions.create_rand_symmetric_matrix_with_defined_cond(10, 1000)
    b2 = A2.dot(x_ex)
    list_of_b2.append(b2)
    db = b2
    for i in range(16):
        db = db + 0.1
        list_of_b2.append(db)
    functions.write_to_file_matrix(A2, "A2.csv")
    functions.write_to_file_matrix(list_of_b2, "b2.csv")

    return list_of_b2


list_of_b2 = data_for_2_graph()