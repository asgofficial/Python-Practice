import numpy as np
from scipy.linalg import eig
from scipy.linalg import lu

A = np.array([
    [4, 3, 2, 1],
    [2, 5, 1, 3],
    [1, 2, 4, 2],
    [3, 1, 2, 5]
])

print("Original Matrix:")
print(A)

eigenvalues, eigenvectors = eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

P, L, U = lu(A)

print("\nPermutation Matrix (P):")
print(P)

print("\nLower Triangular Matrix (L):")
print(L)

print("\nUpper Triangular Matrix (U):")
print(U)