import math_extended

def main():
    try:
        num = float(input("Enter a number to find the square root: "))
        sqrt_result = math_extended.find_square_root(num)
        print(f"Square root of {num} is {sqrt_result:.2f}")

        a = int(input("Enter first number for GCD: "))
        b = int(input("Enter second number for GCD: "))
        gcd_result = math_extended.find_gcd(a, b)
        print(f"GCD of {a} and {b} is {gcd_result}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
