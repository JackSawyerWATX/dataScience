import numpy as np

# finds and returns indeces where the value is 4
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)

print(x)

# finds and returns values that are divisible by 2
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)

print(x)

# finds the indeces where the values are odd
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)

print(x)

# searchsorted() returns the index where the specified value would be inserted to maintain the search order
arr = np.array([4, 5, 6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# side='right' will return the rightmost index to insert the element
x = np.searchsorted(arr, 7, side='right')
print(x)


arr = np.array([1, 3, 5, 7])
# Returns the indexes where 2, 4, 6 should be inserted.
x = np.searchsorted(arr, [2, 4, 6])
print(x)



