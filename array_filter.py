import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]
newarr= arr[x]
print(newarr)


# create an empty list
filter_arr = []

#go through each element in arr
for element in arr:
  #if the element is over 42, set the value to True, otherwise set to False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#create an empty list
filter_array = []

# go through each element in the array
for element in arr:
  # if the element is divisible by 2, return True, otherwise return False
  if element %2 == 0:
    filter_array.append(True)
  else:
    filter_array.append(False)

newarray = arr[filter_array]

print(filter_array)
print(newarray)


# Creating filtersdirectly from the array
arr = np.array([60, 61, 62, 63, 64, 65, 66, 67, 68, 69])

filter_arr = arr >= 64
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


another_filter = arr % 2 == 0
newarr = arr[another_filter]

print(another_filter)
print(newarr)