from numpy import random

# Zipf's Law: In a collection, the nth common term is 1/n times of the 
# most common term. e.g. the 5th most common word in English occurs 
# nearly 1/5 times as often as the most common word.
x = random.zipf(a=2, size=(6, 8))
print(x)


# visualization of the zipf distribution
import matplotlib.pyplot as plt
import seaborn as sns

# Sample 1000 points but plotting only ones with value < 10 for 
# more meaningful chart.
x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])

plt.show()

