import numpy as np
from scipy.linalg import qr
from scipy.linalg import svd
from scipy.linalg import lstsq

A = np.array([
    [1, 2],
    [3, 4]
])

print("Original Matrix:")
print(A)


# --------------------------------
# 1. QR Decomposition
# --------------------------------

Q, R = qr(A)

print("\nQ Matrix:")
print(Q)

print("\nR Matrix:")
print(R)


# --------------------------------
# 2. Singular Value Decomposition
# --------------------------------

U, S, Vt = svd(A)

print("\nU Matrix:")
print(U)

print("\nSingular Values:")
print(S)

print("\nV Transpose:")
print(Vt)


# --------------------------------
# 3. Least Squares
# --------------------------------

B = np.array([5, 11])

x, residuals, rank, singular_values = lstsq(A, B)

print("\nSolution using Least Squares:")
print(x)

print("\nResiduals:")
print(residuals)

print("\nRank:")
print(rank)

print("\nSingular Values:")
print(singular_values)