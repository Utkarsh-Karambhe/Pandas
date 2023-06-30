import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(123)
time_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']
productivity_levels = np.random.randint(1, 6, size=100)  
data = pd.DataFrame({'TimeOfDay': np.random.choice(time_of_day, size=100),
                     'ProductivityLevel': productivity_levels})
average_productivity = data.groupby('TimeOfDay')['ProductivityLevel'].mean().reset_index()
sns.barplot(x='TimeOfDay', y='ProductivityLevel', data=average_productivity)
plt.xlabel('Time of the Day')
plt.ylabel('Productivity Level')
plt.title('Productivity Level by Time of the Day')
plt.show()
