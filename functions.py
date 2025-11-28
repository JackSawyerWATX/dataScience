import numpy as np

maximum = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print("Maximum: ..................", maximum)

minimum = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print("Minimum: ..................", minimum)

length = len([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
print("Length: ...................", length)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    numbers = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
    average = calculate_average(numbers)
    print("Average using function: ...", average)

numbers = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
mean_numbers = np.mean(numbers)
print("Mean using NumPy: .........", mean_numbers)

# np.mean lets the Python library know that I want to use the mean function from the Numpy library