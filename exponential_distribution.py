from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# makes a samplefor exponential distribution with 2.0 scale and size is 4 arrays with 6 elements
x = random.exponential(scale=2.0, size=(4, 6))
np.set_printoptions(threshold=np.inf)
print(x)


# A visualizatiion of exponential distribution
sns.displot(random.exponential(size=1000), kind='kde')
plt.show()

# The difference between Exponential, Normal, Logistic, Uniform, Poisson, and Binomial distribution
data = {
  "exponential": random.exponential(scale=2.0, size=1000),
  "normal": random.normal(loc=0, scale=10, size=1000),
  "logistic": random.logistic(loc=0, scale=10, size=1000),
  "uniform": random.uniform(low=0, high=10, size=1000),
  "poisson": random.poisson(lam=10, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}
sns.displot(data, kind='kde')
plt.show()


# Exponential distribution is used for describing time till next event 
# e.g. failure/success etc.
# It has two parameters:
#   scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#   size - The shape of the returned array.