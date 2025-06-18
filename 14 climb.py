def climb_stairs(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]

# Example usage
n = 4
print(f"Number of distinct ways to climb {n} steps:", climb_stairs(n))
