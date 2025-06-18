# 1. Number Series: Generate Fibonacci up to n terms
def fibonacci_series(n):
    print("\nFibonacci Series:")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# 2. Number Pattern: Right-angled triangle number pattern
def number_triangle(rows):
    print("\nNumber Triangle Pattern:")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# 3. Pyramid Pattern: Centered star pyramid
def star_pyramid(rows):
    print("\nStar Pyramid Pattern:")
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

# ----------- Main Program -----------

# Number Series
n = int(input("Enter number of terms for Fibonacci series: "))
fibonacci_series(n)

# Number Pattern
rows = int(input("Enter number of rows for number pattern: "))
number_triangle(rows)

# Pyramid Pattern
pyramid_rows = int(input("Enter number of rows for star pyramid: "))
star_pyramid(pyramid_rows)
