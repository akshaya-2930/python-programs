# Sample dictionary
my_dict = {
    'a': 2,
    'b': 3,
    'c': 2,
    'd': 4,
    'e': 3
}

# Create an empty dictionary to store frequency of values
frequency = {}

# Count frequency of each value
for value in my_dict.values():
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

# Display the result
print("Frequency of elements (values) in the dictionary:")
for val, count in frequency.items():
    print(f"{val}: {count}")
