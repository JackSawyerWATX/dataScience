from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

# generates a sample for rayleigh distriibution with a scale of 10 and a size of 4x5
x = random.rayleigh(scale=10, size=(4, 5))
print(x)

# visualization of the rayleigh dsitribution
sns.displot(random.rayleigh(scale=10, size=1000), kind="kde")
plt.show()

# comparison of rayleigh to other distribution methods
data = {
  "exponential": random.exponential(scale=1, size=1000),
  "normal": random.normal(loc=0, scale=10, size=1000),
  "logistic": random.logistic(loc=0, scale=10, size=1000),
  "uniform": random.uniform(low=0, high=10, size=1000),
  "poisson": random.poisson(lam=10, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000),
  "chi-square": random.chisquare(df=10, size=1000),
  "rayleigh": random.rayleigh(scale=10, size=1000)
}

sns.displot(data, kind='kde')
plt.show()