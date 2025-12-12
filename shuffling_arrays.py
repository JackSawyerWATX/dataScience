import numpy as np
from numpy import random

# randomlly shuffle elements of the array
# the shuffle method makes changes to rhe array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
random.shuffle(arr)
print(arr)

# returns a re-arranged copy of the array and leaves the original array unchanged
print(random.permutation(arr))

