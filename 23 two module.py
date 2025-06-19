def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()
from .math_utils import add, subtract
from .string_utils import to_uppercase, to_lowercase
from utilities import add, subtract, to_uppercase, to_lowercase

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Uppercase:", to_uppercase("hello"))
print("Lowercase:", to_lowercase("WORLD"))
