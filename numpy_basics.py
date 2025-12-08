import numpy as np

arr =np.array([1, 2, 3, 4, 5, 6, 7])
tup = np.array((1, 2, 3, 4, 5))

print(arr)
print("NumPy version:", np.__version__)
print("Array type:", type(arr))
print("Tuple converted to array:", tup)

zero_d_arr = np.array(42)
print("0-D array:", zero_d_arr)

one_d_array = np.array([1, 2, 3, 4, 5])
print("1-D array:", one_d_array)

two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D array:\n", two_d_array)

three_d_array = np.array([[[1, 2, 3], [3, 4, 5]], [[5, 6, 7], [7, 8, 9]]])
print("3-D array:\n", three_d_array)

print(zero_d_arr.ndim, "dimension(s)")
print(one_d_array.ndim, "dimension(s)")
print(two_d_array.ndim, "dimension(s)")
print(three_d_array.ndim, "dimension(s)")

five_d_array = np.array([1, 2, 3, 4], ndmin=5)
print("5-D array:\n", five_d_array)
print(five_d_array.ndim, "dimension(s)")

anotherArr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("second from last element from 2nd dimension: ", anotherArr[1, -2])

# Slice elements from first index to index 5
print(arr[1:5])

# Slice elements from index 4 to the end of the array
print(arr[:4])

# Slice elements from the beginning up to, but not including index 4
print(arr[4:])

# Use the minus (-) operator to reference an index from the end of the array
print(arr[-4:-1])

# Use the step value to determine the increment of slicing
print(arr[1:5:2])

# Return every other element from the array
print(arr[::2])

# Return every third element from the array
print(arr[::3])

# Start at the second element and slice elements from index 1 up to but not including index 4
print(anotherArr[1, 1:4])

# Return index 2 from both arrays
print(anotherArr[0:2, 2])

# From both elements, slice index 1 up to but not including index 4, and return a 2-D array
print(anotherArr[0:2, 1:4])

print(arr.dtype)

print(anotherArr.dtype)

fruits = np.array(['apple', 'banana', 'pineapple'])

print(fruits.dtype)
