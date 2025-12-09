import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# joins or concatinates two or more arrays
arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# joins two arrays along rows, otherwise known as axis 1.
arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

# joins two arrays along columns, otherwise known as axis 0.
arr = np.concatenate((arr1, arr2), axis=0)
arr = np.stack((arr1, arr2), axis=1)

print(arr)

# this is called a helper function that stacks along rows
arr = np.hstack((arr1, arr2))

print(arr)

# this uses a helper function that stacks along columns
arr = np.vstack((arr1, arr2))

print(arr)

# this uses a helper function that stacks along height, otherwise known as depth.
arr = np.dstack((arr1, arr2))

print(arr)