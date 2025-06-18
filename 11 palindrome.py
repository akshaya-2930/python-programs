def is_palindrome(number):
    original = str(number)
    reversed_num = original[::-1]
    return original == reversed_num

# Example usage
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
