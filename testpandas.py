import matplotlib.pyplot as plt

# Column Chart
categories = ['Category A', 'Category B', 'Category C']
values = [25, 40, 30]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Column Chart')
plt.show()



# Pie Chart
labels = ['Category 1', 'Category 2', 'Category 3']
sizes = [30, 45, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

# Heat Map
import numpy as np

data = np.random.rand(5, 5)

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heat Map')
plt.show()

# Lollipop Plot
categories = ['Category X', 'Category Y', 'Category Z']
values = [10, 25, 15]

plt.stem(categories, values, linefmt='C0-', markerfmt='C0o', basefmt='k-')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Lollipop Plot')
plt.show()

