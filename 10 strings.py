# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Count characters in a string
def character_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

# 3. Replace characters in a string
def replace_characters(s, old, new):
    return s.replace(old, new)

# ----------- Main Program -----------

# Input string
text = input("Enter a string: ")

# Reverse
reversed_text = reverse_string(text)
print("\nReversed String:", reversed_text)

# Character Count
counts = character_count(text)
print("\nCharacter Count:")
for char, cnt in counts.items():
    print(f"{char}: {cnt}")

# Replace characters
old_char = input("\nEnter character to replace: ")
new_char = input("Enter new character: ")
replaced_text = replace_characters(text, old_char, new_char)
print("Updated String:", replaced_text)
