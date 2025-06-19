def divide_numbers():
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def check_voter_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age >= 18:
            print("Eligible to vote.")
        else:
            print("Not eligible to vote.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def validate_student_marks():
    try:
        marks = float(input("Enter student marks (0 to 100): "))
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
        print(f"Marks entered: {marks}")
    except ValueError as e:
        print(f"Invalid input: {e}")

# Run the applications
divide_numbers()
check_voter_eligibility()
validate_student_marks()
