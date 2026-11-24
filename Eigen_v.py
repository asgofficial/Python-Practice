'''
4.1. Create  a square matrix of 4*4 order and find out the eigen value and eigen vector of the matrix.

    4.2. Find out P,L and U of the matrix.
'''

import numpy as np

A = np.array([[4, 1, 0, 0],
              [1, 4, 1, 0],
              [0, 1, 4, 1],
              [0, 0, 1, 4]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

import numpy as np
from scipy.linalg import lu

A = np.array([[4, 1, 0, 0],
              [1, 4, 1, 0],
              [0, 1, 4, 1],
              [0, 0, 1, 4]])

P, L, U = lu(A)

print("P Matrix:")
print(P)

print("\nL Matrix:")
print(L)

print("\nU Matrix:")
print(U)
