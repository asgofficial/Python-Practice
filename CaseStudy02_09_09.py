'''
    1.Consider the following linear eqn and solve using SciPy:
    2x + 3y = 8
    4x + 5y = 14

    2. Consider a scenario where 2 cars are moving. 1 car from a point P and the other car from point Q
     in the same direction and meet each other after 11 hours. If they move in the opposite direction,
     they will meet after one hour. Find out the velocity of both cars.

    3. Create the matrix of 4*4 order and find out the transpose of the matrix and the rank of the
    matrix using SciPy.
'''

import numpy as np
from scipy.linalg import solve

A = np.array([[2, 3], [4, 5]])
B = np.array([8, 14])

result = solve(A, B)

print("x =", result[0])
print("y =", result[1])

d = float(input("Enter distance between P and Q: "))

u = (6 * d) / 11
v = (5 * d) / 11

print("Velocity of Car 1 =", u, "km/hr")
print("Velocity of Car 2 =", v, "km/hr")

import numpy as np
from scipy.linalg import svdvals

A = np.array([[1, 2, 3, 4],
              [2, 4, 6, 8],
              [3, 5, 7, 9],
              [4, 6, 8, 10]])

print("Original Matrix:")
print(A)

print("Transpose:")
print(A.T)

s = svdvals(A)
rank = np.sum(s > 1e-10)

print("Rank of Matrix:", rank)
