from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generates a random 1x10 distribution for occurrence 2
x = random.poisson(lam=2, size=12)
print(x)

# Visualization of Poisson distribution
sns.displot(random.poisson(lam=2, size=1000), kind='kde')
plt.show()

# The difference between Normal, Poisson, and Binomial distribution
data = {
  "Normal": random.normal(loc=70, scale=10, size=(1000)),
  "Poisson": random.poisson(lam=55, size=1000),
  "Binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind='kde')
plt.show()



# Poisson Distribution is a Discrete Distribution.
# It expresses the probability of a given number of events occurring in a fixed interval of time or space
# if these events occur with a known constant mean rate and independently of the time since the last event.
# It has two parameters:
#   lam - expected number of occurrences within the given interval.
#   size - The shape of the returned array.
