import numpy as np

# deletes the repeted values and returns the new array
arr = np.array([1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7])
x = np.unique(arr)
print(x)

# combines teh two arrays and omits the repeted values
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)

# finds the common values between two arrays
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)

# finds the values in arr1 that are not in arr2
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr)

# finds the values in arr2 that are not in arr1
newarr = np.setdiff1d(arr2, arr1, assume_unique=True)
print(newarr)

# finds the values that are not common in both arrays
newarr = np.setxor1d(arr1, arr2, assume_unique=True)
print(newarr)