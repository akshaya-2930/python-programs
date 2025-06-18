def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_even_numbers(original_list)

print("Original list:", original_list)
print("List after removing even numbers:", filtered_list)
