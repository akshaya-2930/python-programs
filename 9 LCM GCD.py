# Function to find GCD using Euclidean algorithm
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find LCM using GCD
def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return (a * b) // gcd

# Main program
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    gcd = find_gcd(num1, num2)
    lcm = find_lcm(num1, num2)

    print("GCD of", num1, "and", num2, "is:", gcd)
    print("LCM of", num1, "and", num2, "is:", lcm)

except ValueError:
    print("Please enter valid integers.")
