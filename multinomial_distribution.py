from numpy import random
import numpy as np

# Creates a 1000 samples from a multinomial distribution
np.set_printoptions(threshold=np.inf)
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=1000)

print(x)