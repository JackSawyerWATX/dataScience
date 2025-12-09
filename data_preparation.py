import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.dropna(axis=0,inplace=True)

print("First 5 lines of data:")
print(health_data.head())
print()
print("Full data sheet:")
print(health_data)
print()
print("Information:")
print(health_data.info())
print()
print("Description:")
print(health_data.describe())



# 1. Import the Pandas library as pd
# 2. Read the CSV file named data.csv using the function pd.read_csv()
# 3. The CSV file is comma-separated and has a header row