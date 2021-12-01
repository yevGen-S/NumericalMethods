import numpy as np
from matplotlib import pyplot as plt
from functions import *

A = np.array([[15,1,2,3,4],
              [1,16,3,4,5],
              [1,2,17,4,5],
              [1,2,3,18,5],
              [1,2,3,4,19]])

write_to_file_matrix(A, "A.csv")
x = np.array([1,1,1,1,1])

res = A.dot(x)
print(res)