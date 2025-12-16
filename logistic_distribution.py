from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creates a 1000 x 1500 sample from a logistic distribution with mean at 5 
# and standard deviation at 10.
# the next line prints out every element in the array to the terminal, 
# instead of a concatenated version.
np.set_printoptions(threshold=np.inf)
x = random.logistic(loc=5, scale=10, size=(1000, 1500))
print(x)

# A visualizatiion of logistic distribution
sns.displot(random.logistic(size=1000), kind='kde')
plt.show()

# The difference between Normal, Logistic, Uniform, Poisson, and Binomial distribution
data = {
  "normal": random.normal(loc=0, scale=10, size=1000),
  "logistic": random.logistic(loc=0, scale=10, size=1000),
  "uniform": random.uniform(low=0, high=10, size=1000),
  "poisson": random.poisson(lam=10, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind='kde')
plt.show()