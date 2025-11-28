import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.plot(x ='Average_Pulse', y ='Calorie_Burnage', kind ='line'),
plt.ylim(ymin = 0)
plt.xlim(xmin = 0)

plt.show()

plt.savefig("health_plot.jpg")
plt.close()