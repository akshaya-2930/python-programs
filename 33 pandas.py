import pandas as pd
import numpy as np

# Step 1: Generate a DataFrame with random salaries
num_employees = 10
data = {
    "EmployeeID": [f"E{100+i}" for i in range(num_employees)],
    "Salary": np.random.randint(5000, 99001, size=num_employees)  # Range: 5000 to 99000
}
df = pd.DataFrame(data)

# Step 2: Filter employees with Salary > 50,000
high_earners = df[df["Salary"] > 50000]

# Output
print("Full Salary Data:\n", df)
print("\nEmployees with Salary > 50,000:\n", high_earners)
