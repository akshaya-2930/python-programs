import numpy as np

# Generate a random 4x4 matrix with integers from 0 to 9
matrix = np.random.randint(0, 10, size=(4, 4))

# Calculate the determinant
determinant = np.linalg.det(matrix)

# Display the matrix and its determinant
print("Random 4x4 Matrix:\n", matrix)
print(f"\nDeterminant: {determinant:.2f}")
