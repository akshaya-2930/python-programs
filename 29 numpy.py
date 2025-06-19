import numpy as np

# Define two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Element-wise addition
addition_result = np.add(matrix1, matrix2)

# Element-wise multiplication
multiplication_result = np.multiply(matrix1, matrix2)

# Display results
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Element-wise Addition:\n", addition_result)
print("Element-wise Multiplication:\n", multiplication_result)
Matrix 1:
 [[1 2]
  [3 4]]
Matrix 2:
 [[5 6]
  [7 8]]
Element-wise Addition:
 [[ 6  8]
  [10 12]]
Element-wise Multiplication:
 [[ 5 12]
  [21 32]]
