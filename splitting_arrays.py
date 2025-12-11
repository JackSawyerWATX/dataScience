import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

# Split `arr` into 3 sub-arrays. If the length of `arr` is not divisible by 3,
# `np.array_split` distributes the leftover elements one per sub-array from
# left to right. For example, length 14 -> sizes [5, 5, 4].
newarr = np.array_split(arr, 3)

print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])


print()
print("splitting 2D arrays")

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr, end="\n")


print()
print("Splitting 2D array into 3 sub-arrays")

# splits the array into three 2D arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# splits the array into three 2D arrays along columns
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

# alternate solution uses hsplit() to split the array into three 2D arrays along columns
newarr = np.hsplit(arr, 3)
print("uses hsplit() method: \n", newarr)