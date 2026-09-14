import numpy as np

A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

B = np.array([
    [2, 1, 3],
    [1, 0, 2],
    [4, 1, 1]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

A_inverse = np.linalg.inv(A)

print("\nInverse of Matrix A:")
print(A_inverse)

det_B = np.linalg.det(B)

print("\nDeterminant of Matrix B:")
print(det_B)

result = np.dot(A, A_inverse)

print("\nA × A inverse:")
print(result)