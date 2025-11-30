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


# Summary — what this script does and important notes
# 1) Uses the Matplotlib 'Agg' backend so plotting works without a display (headless).
# 2) Loads `data.csv` into a Pandas DataFrame (expects a header row with columns
#    including `Average_Pulse` and `Calorie_Burnage`).
# 3) Calls `health_data.plot(...)` to draw `Calorie_Burnage` vs `Average_Pulse`.
#    Note: there is a trailing comma after the plot call which creates a 1-tuple;
#    remove the comma to avoid confusion (the plot will still be produced).
# 4) Sets axis limits (x >= 0, y >= 0) to keep the plot range non-negative.
# 5) `plt.show()` is present but with 'Agg' backend it will not open a GUI window.
#    To view interactively, remove `matplotlib.use('Agg')` and run in a GUI-capable
#    environment (or use Jupyter); otherwise prefer saving to a file.
# 6) Saves the figure to `health_plot.jpg` and closes the figure to free resources.
# 7) Optional: to stream binary PNG to stdout (for piping), use
#    `plt.savefig(sys.stdout.buffer, format='png')` and redirect the process output
#    to a file (PowerShell example: `py plottingFunctions.py > out.png`).
# 8) Recommendation: coerce plotting columns to numeric (e.g. `pd.to_numeric(...,
#    errors='coerce')`) and drop NaNs before plotting to avoid plot errors or
#    unexpected gaps caused by non-numeric values like 'AF' or '9 000'.