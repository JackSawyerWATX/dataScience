import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.plot(x ='Average_Pulse', y ='Calorie_Burnage', kind ='line'),
plt.ylim(ymin = 0)
plt.xlim(xmin = 0)

plt.show()

plt.savefig("health_plot.jpg")
plt.close()


# 1. Set Matplotlib backend to 'Agg' so plotting works without a display 
#    (headless/scripted use).
# 2. Import Matplotlib's pyplot and Pandas for plotting and data handling.
# 3. Read `data.csv` from the current directory into a Pandas DataFrame (expects 
#    a header row).
# 4. Create a line plot with `Average_Pulse` on the x-axis and `Calorie_Burnage` 
#    on the y-axis. Set the kind of line plot to 'line'.
# 5. Set the y-axis lower limit to 0 and the x-axis lower limit to 0 (prevents 
#    negative axis ranges).
# 6. Call `plt.show()` Note: when using the 'Agg' backend this will not display 
#    a GUI window; it's harmless but typically not used in headless scripts.
# 7. Save the plot to `health_plot.jpg` and close the figure.
# 8. Optional: to stream binary PNG to stdout for piping, replace the file save 
#    with `plt.savefig(sys.stdout.buffer, format='png')` and redirect output to a file (e.g., `py plottingFunctions.py > out.png`).