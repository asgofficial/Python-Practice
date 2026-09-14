import numpy as np
from scipy.linalg import solve

A = np.array([
    [2, 3],
    [4, 5]
])

B = np.array([8, 14])

x, y = solve(A, B)

print("Value of x:", x)
print("Value of y:", y)