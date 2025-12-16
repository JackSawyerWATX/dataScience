from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# makes a sample for chi-square distribution with 3 degrees of freedom and 
# size is 7 arrays with 9 elements
x = random.chisquare(df=3, size=(7, 9))
print(x)


# A visualization of chi-square distribution
sns.displot(random.chisquare(df=1, size=1000), kind='kde')
plt.show()


# the difference between Exponential, Normal, Logistic, Uniform, Poisson, 
# Binomial and Chi-Square distribution
data = {
  "exponential": random.exponential(scale=2.0, size=1000),
  "normal": random.normal(loc=0, scale=10, size=1000),
  "logistic": random.logistic(loc=0, scale=10, size=1000),
  "uniform": random.uniform(low=0, high=10, size=1000),
  "poisson": random.poisson(lam=10, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000),
  "chi-square": random.chisquare(df=3, size=1000)
}
sns.displot(data, kind='kde')
plt.show()


# Chi-square distribution is used in hypothesis testing and construction of confidence intervals.
# It has two parameters:
#   df - degrees of freedom, must be positive integer.
#   size - The shape of the returned array.
