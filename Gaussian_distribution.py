from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# gets a normal (Gaussian) data distribution
x = random.normal(size=(2, 3))
print(x)

print()

# gets a normal (Gaussian) data distribution with specified mean (loc)
x = random.normal(loc=1, scale=2, size=(3, 5))
print(x)

# visualization on Gaussian distribution
sns.displot(random.normal(size=1000), kind='kde')
plt.show()