import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import os

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data['Average_Pulse'] = pd.to_numeric(health_data['Average_Pulse'], errors='coerce')
health_data['Calorie_Burnage'] = pd.to_numeric(health_data['Calorie_Burnage'], errors='coerce')

health_data = health_data.dropna(subset=['Average_Pulse', 'Calorie_Burnage'])

ax = health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line')
ax.set_ylim(0, 400)
ax.set_xlim(0, 150)

out_path = 'plot.png'
plt.savefig(out_path, bbox_inches='tight', format='png')
plt.close()

try:
    os.startfile(out_path)
except Exception:
    print(f"Saved plot to {out_path}. Please open it to view the graph.")

# Summary of what this program does:
# 1. Uses the Matplotlib 'Agg' backend so the script can run without a display (headless).
# 2. Reads 'data.csv' into a Pandas DataFrame.
# 3. Coerces 'Average_Pulse' and 'Calorie_Burnage' columns to numeric; invalid values become NaN.
# 4. Drops rows missing either of those numeric values before plotting.
# 5. Plots 'Calorie_Burnage' versus 'Average_Pulse' as a line plot and sets axis limits.
# 6. Saves the plot to 'plot.png'.
# 7. Attempts to open the saved image with the OS default image viewer on Windows; if that fails, prints the path.
#
# Optional notes:
# - To capture binary PNG output on stdout instead of saving to a file, you can use:
#   `plt.savefig(sys.stdout.buffer, format='png')` and then redirect the process output to a file.
# - If you want to view the plot interactively, remove the `matplotlib.use('Agg')` line and run in an environment with a GUI (or use Jupyter), then call `plt.show()`.
