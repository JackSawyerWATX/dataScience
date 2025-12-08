import numpy as np

# the original array is NOT affected by changes made using copy().
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


# the original array is affected by changes made using array().
arr2 = np.array([1, 2, 3, 4, 5])
y = arr2.view()
arr2[0] = 31

print(arr2)
print(y)


arr3 = np.array([10, 11, 12, 13, 14, 15])

a = arr3.copy()
b = arr3.view()

print("Check array data ownership")
print(a.base)
print(b.base)