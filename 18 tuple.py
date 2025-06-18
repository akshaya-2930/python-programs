def find_max_min(tup):
    if not tup:
        return None, None
    return max(tup), min(tup)

# Example usage
sample_tuple = (23, 1, 45, 76, 12, 3)
maximum, minimum = find_max_min(sample_tuple)

print("Tuple:", sample_tuple)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
