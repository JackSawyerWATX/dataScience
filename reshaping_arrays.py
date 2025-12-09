import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# reshapes the array from 1D to 2D.
newArr = arr.reshape(3, 4)
print(newArr)

# reshaped the array to a different 2D
anotherArray = arr.reshape(4, 3)
print(anotherArray)

# reshaped to a 3D array, and used -1 to define an unknown deminsion.
yetAnotherArray = arr.reshape(2, 3, -1)
print(yetAnotherArray)

# shows whether the reshaped array is a view or a copy of the original array.
print(arr.reshape(3, 4).base)