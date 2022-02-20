import numpy as np
from math import cos

def chebyshev_grid(a, b, n):
    grid = np.array([(b - a) * 0.5 * np.cos(np.pi * (2 * i + 1) / (2 * n))
                     + (a + b) * 0.5 for i in range(n-1, -1, -1)])

    # if not a in grid:
    #     grid = np.insert(grid, 0, a)
    # if not b in grid:
    #     grid = np.append(grid, b)
    return grid
