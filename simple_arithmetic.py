import numpy as np

# first set of arrays for the first three examples
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# addition
newarr = np.add(arr1, arr2)
print(newarr)

# subtraction
newarr = np.subtract(arr1, arr2)
print(newarr)

# multiplication
newarr = np.multiply(arr1, arr2)
print(newarr)

# second set of arrays for the next group of examples
arr3 = np.array([10, 20, 30, 40, 50, 60])
arr4 = np.array([3, 5, 10, 8, 2, 33])

# divide
newarr = np.divide(arr3, arr4)
print(newarr)

# raises the values in array1 to the values in arr2
newarr = np.power(arr3, arr4)
print(newarr)

# returns the remainders
newarr = np.mod(arr3, arr4)
print(newarr)

# returns the same thing as the mod() function
newarr = np.remainder(arr3, arr4)
print(newarr)

# returns the quotient and the mod
newarr = np.divmod(arr3, arr4)
print(newarr)

# new array for the last example
arr5 = np.array([-1, -2, -3, -4, -5])

# returns the absolute values of the array
newarr = np.absolute(arr5)
print(newarr)