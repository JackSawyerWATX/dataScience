import pandas as pd
import matplotlib.pyplot as plt

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

full_health_data = full_health_data.dropna(subset=["Duration", "Max_Pulse"])

full_health_data.plot(x ='Duration', y='Max_Pulse', kind='scatter')

plt.show()