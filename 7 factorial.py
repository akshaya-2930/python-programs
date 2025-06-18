import math

# 1. Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 2. Function to find the largest number in a list
def find_largest(numbers):
    if not numbers:
        return "List is empty"
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

# 3. Function to calculate area of a shape
def area_of_shape(shape, *dimensions):
    shape = shape.lower()
    if shape == "rectangle" and len(dimensions) == 2:
        return dimensions[0] * dimensions[1]
    elif shape == "circle" and len(dimensions) == 1:
        return math.pi * dimensions[0] ** 2
    else:
        return "Invalid shape or dimensions"

# Example usage
print("Factorial of 5 is:", factorial(5))
print("Largest in [4, 15, 2, 89, 32] is:", find_largest([4, 15, 2, 89, 32]))
print("Area of rectangle (5, 3):", area_of_shape("rectangle", 5, 3))
print("Area of circle (radius 4):", area_of_shape("circle", 4))
