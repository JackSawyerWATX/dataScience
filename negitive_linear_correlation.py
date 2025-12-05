import pandas as pd
import matplotlib.pyplot as plt

# x axis
negative_corr = {'Hours_Work_Before_Training': [10,9,8,7,6,5,4,3,2,1],

# calories burned
'Calorie_Burnage': [220,240,260,280,300,320,340,360,380,400]}

# converts x axis data into a data frame
# You could write negative_corr = pd.DataFrame(negative_corr) (the data= is optional)
negative_corr = pd.DataFrame(data=negative_corr)

# plots and assigns the data and declares the output to be scatter
negative_corr.plot(x ='Hours_Work_Before_Training', y='Calorie_Burnage', kind='scatter')

plt.show() 