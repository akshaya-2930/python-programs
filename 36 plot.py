import matplotlib.pyplot as plt

# Data points
X = [1, 2, 3, 4, 5]
Y = [2, 4, 1, 3, 7]

# Create scatter plot
plt.scatter(X, Y, color='green', marker='o')

# Add titles and labels
plt.title('Scatter Plot Example')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)

# Display the plot
plt.show()
