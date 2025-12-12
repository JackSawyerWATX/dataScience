import matplotlib.pyplot as plt
import seaborn as sns

# plots a displot without a histogram  by adding kind="kde"
sns.displot([0, 11, 32, 53, 74, 95, 26, 47, 68, 89, 110], kind="kde")
plt.show()
