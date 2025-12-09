import pandas as pd

d = {
  'column1' : [1, 2, 3, 4, 5], 
  'column2' : [6, 7, 8, 9, 10], 
  'column3' : [11, 12, 13, 14, 15 ]
}

dataFrame = pd.DataFrame(data=d)

print(dataFrame)

print()

column_count = dataFrame.shape[1]
print(f"Number of Columns: ... ", column_count)

row_count = dataFrame.shape[0]
print(f"Number of Rows: ...... ", row_count)

# 1. Import the Pandas library as pd
# 2. Define data with column and rows in a variable named d
# 3. Create a data frame using the function pd.DataFrame()
# 4. The data frame contains 3 columns and 5 rows
# 5. Print the data frame output with the print() function
# 6. Prints out the number of Columns
# 7. Prints out the number of Rows

