import matplotlib.pyplot as plt

# Data
products = ['A', 'B', 'C', 'D']
sales = [40, 60, 80, 100]

# Create bar chart
plt.bar(products, sales, color='skyblue')
plt.title('Sales of Different Products')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.show()
