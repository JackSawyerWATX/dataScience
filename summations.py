import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# adds each number in the array to the same number in the next array, according
# to the index and returns a new array.
newarr = np.add(arr1, arr2)
print(newarr)

# adds all the numbers in both arrays and returns a total
newarr = np.sum([arr1, arr2])
print(newarr)

# the summation over one axis is an addition of all the numbers in each array 
# totaled. By adding axis=1, this adds each array and returns a total for 
# that array before doing the same to the next array.
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

# cummulative sum returns an array of all numbers in the array added together, cummulativly.
# for example:
#   the array [1, 2, 3, 4] used here, 
#   returns[1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4] = [1, 3, 6, 10]
newarr = np.cumsum(arr1)
print(newarr)