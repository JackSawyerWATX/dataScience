from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Create a 4 x 6 uniform distribution multi dimensional array
x = random.uniform(size=(4, 6), low=(10), high=(1200))
print(x)

# Visualization of Uniform distribution
sns.displot(random.uniform(low=12, high=72, size=1000), kind='kde')
plt.show()


# Uniform Distribution
# Used to describe probability where every event has equal chances of occurring.
# It has three parameters:
#   low - lower bound - default 0.0
#   high - upper bound - default 1.0
#   size - The shape of the returned array.