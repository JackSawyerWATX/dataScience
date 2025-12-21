import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# finds the product in the array
a = np.prod(arr1)
print(a)

# multiplys both arrays
b = np.prod([arr1, arr2])
print(b)

# multiplys bothe arrays individually and returns their product
c = np.prod([arr1, arr2], axis=1)
print(c)

# returns a cumulative product of all numbers in the array
d = np.cumprod(arr2)
print(d)

