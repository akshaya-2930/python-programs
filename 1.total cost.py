items = [
    {"name": "Apples", "price": 30.0, "quantity": 2},
    {"name": "Milk", "price": 25.5, "quantity": 1},
    {"name": "Bread", "price": 20.0, "quantity": 3}
]

# Initialize total cost
total_cost = 0.0

# Calculate total cost
for item in items:
    item_cost = item["price"] * item["quantity"]
    print(f"{item['name']}: ₹{item['price']} × {item['quantity']} = ₹{item_cost}")
    total_cost += item_cost

# Display total bill
print(f"\nTotal Bill: ₹{total_cost}")
