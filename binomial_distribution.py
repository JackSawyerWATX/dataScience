from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# given 10 trials for a coin toss, generate 10 data points.
x = random.binomial(n=10, p=0.5, size=10)
print(x)

# Example Array: [4 2 6 5 3 5 6 6 6 4]
# Each integer in the array is 10 coin flips. This first integer in 
# this array turned out to be 4 times the coin landed on heads, the 
# second integer being that it landed on heads 2 out of ten times, 
# the third being 6 out of 10, and so on.


# binomial visualization
# sns.displot(random.binomial(n=10, p=0.5, size=1000))
# plt.show()


# This generates random data from different distributions
data = {
  "Normal": random.normal(loc=50, scale=5, size=(1000)),
  "Binomial": random.binomial(n=100, p=0.5, size=1000),
}

sns.displot(data, kind='kde')
plt.show()


# Binomial Distribution is a Discrete Distribution.
# It describes the outcome of binary scenarios, e.g. toss of a coin, 
# it will either be head or tails.

# It has three parameters:
#   n - number of trials.
#   p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
#   size - The shape of the returned array.

# Discrete Distribution:The distribution is defined at separate set of events, 
# e.g. a coin toss's result is discrete as it can be only head or tails whereas 
# height of people is continuous as it can be 170, 170.1, 170.11 and so on.