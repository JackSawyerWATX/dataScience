import numpy as np

# finds the sine value of pi / 2
x = np.sin(np.pi/2)
print(x)

# finds the sine values for all values in arr
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

# finds the cosine value of pi / 2
x = np.cos(np.pi/2)
print(x)

# converts all values in following array to radians
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

# convert all of the values in following array to degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

# finds the angle of 1.0
x = np.arcsin(1.0)
print(x)

# finds teh angle for all the sine values in the array
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

# finds teh hypotenues for base 4 and 3 perpendicular
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)