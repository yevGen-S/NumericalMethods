from integration3_8 import integration3_8__2
import numpy as np


def fun(x):
    return np.sin(x)

print(integration3_8__2(fun,a=0, b = np.pi /2 ,eps =1e-15))