import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# prints the shape of the array as 2 intigers inside a tuple.
# first number being the size of the outer array, and the second being the size inside both arrays.
# Both arrays must be homogeneous, or the same size.
print("Array shape:", arr.shape)

arr2 = np.array([1, 2, 3, 4, 5], ndmin=5)

# prints out the array.
print(arr2)

# prints out the dimentions of the array
print(arr2.shape)

