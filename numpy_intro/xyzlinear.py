import numpy as np

# Coefficients matrix
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

# Constants vector
b = np.array([8, -11, -3])

solution = np.linalg.solve(A, b)
print(f"Solution: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")