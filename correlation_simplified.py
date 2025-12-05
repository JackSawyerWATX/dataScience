import pandas as pd
import matplotlib.pyplot as plt

# this cleans the data
health_data = pd.read_csv("data.csv", header=0, sep=",", thousands=" ", skipinitialspace=True)

# this converts it to metric and removes any internal spaces
health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='scatter')

# this deletes any rows with missing values
health_data = health_data.dropna(subset=['Average_Pulse', 'Calorie_Burnage'])

plt.show()