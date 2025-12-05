# Python Libraries

The project uses the following Python libraries:

- **Pandas**: used for structured data operations (importing files, creating DataFrames, and data preparation).
- **NumPy**: numerical operations and N-dimensional arrays.
- **Matplotlib**: plotting and visualization.
- **SciPy**: scientific utilities, including linear algebra modules.


## Project Overview

This workspace contains small Python scripts for data preparation, plotting, and array utilities. A CSV file named `data.csv` is expected to be present in the same folder for the data-preparation and plotting scripts.

### How to run (PowerShell)

```powershell
py .\dataPreparation.py
py .\plottingFunctions.py
py .\anArray.py
```

> Note: `plottingFunctions.py` uses a non-interactive Matplotlib backend and saves plots to files (or stdout if modified). See the file descriptions below.


## Dependencies / Installation

Install required packages with pip:

```powershell
py -m pip install pandas numpy matplotlib scipy
```


## Files

- `dataPreparation.py`
  - Reads `data.csv` with robust parsing (delimiter inference and malformed-line handling).
  - Treats common placeholders as missing (`'', 'NA', 'N/A', 'n/a', 'NULL'`) and replaces whitespace-only values with proper NA.
  - Prints diagnostics (`.info()` and `isna().sum()`), then drops rows with any NA using `dropna(axis=0, inplace=True)`.
  - Use this script to create a cleaned dataset before plotting.

- `plottingFunctions.py`
  - Loads `data.csv` (recommended to use cleaned CSV), coerces plotting columns to numeric, and produces a line plot of `Calorie_Burnage` versus `Average_Pulse`.
  - Uses the `Agg` backend for non-interactive/scripted use and saves plots to disk by default. To write binary image data to stdout, call `plt.savefig(sys.stdout.buffer, format='png')` and redirect output from the shell.
  - Remove any trailing commas in the plotting call (e.g., avoid `health_data.plot(...),`).

- `anArray.py`
  - Utility functions demonstrating array reversal:
    - `reverse_in_place(arr)`: reverses a list in place using a two-pointer swap.
    - `reversed_copy(arr)`: returns a reversed copy using slicing (`arr[::-1]`).
  - Running the script prints the original array, a reversed copy, and the array after in-place reversal.

- `slopeAndIntercept.py`
  - Small utility that computes the slope between two points.
  - Contains `slope(x1, y1, x2, y2)` which returns `(y2 - y1) / (x2 - x1)`.
  - The script includes a sample `print(slope(80, 240, 90, 260))` demonstrating usage.

- `NewPLotGraph.py`
  - Script that reads `data.csv`, coerces `Average_Pulse` and `Calorie_Burnage` to numeric types, drops rows with missing values in those columns, and produces a line plot of `Calorie_Burnage` versus `Average_Pulse`.
  - Sets axis limits (x: 0–150, y: 0–400), saves the figure to `plot.png`, and attempts to open the image with the OS default viewer on Windows.
  - Uses the Matplotlib `Agg` backend so it can run headless; optional notes in the script explain how to pipe PNG binary to stdout or run interactively by removing the backend override.

- `standard_deviation.py`
  - Reads `data.csv` with `thousands=' '` to parse numbers like `9 000` correctly.
  - Selects numeric columns and computes per-column statistics: mean and standard deviation.
  - Computes coefficient of variation (std / mean) per column and prints both std and CV.
  - Prints the resulting pandas Series of standard deviations and CV; watch for zero means when interpreting CV.

- `requirements.txt`
  - Lists core dependencies: `pandas`, `numpy`, `matplotlib`, and `scipy`.

- `correlation.py`
  - Reads `data.csv`, coerces `Average_Pulse` and `Calorie_Burnage` to numeric (removing internal spaces), drops rows with missing values, and creates a scatter plot.
  - By default the script will attempt to open the plot interactively and then prompt whether to save it to `correlation_plot.png`.
  - CLI options:
    - `--out FILE` : set output filename (default `correlation_plot.png`).
    - `--no-open` : do not open/show the plot window.
    - `--no-save` : do not save the plot to disk (attempt to show only).
  - The script attempts to select an interactive backend (`TkAgg`) when appropriate and falls back to `Agg` in headless environments.

- `correlation_simplified.py`
  - Minimal helper that reads `data.csv` (handles `thousands=' '` and `skipinitialspace=True`) and produces a scatter plot of `Calorie_Burnage` vs `Average_Pulse` using `DataFrame.plot(kind='scatter')`.
  - Calls `plt.show()` to display the plot; it is intended for interactive use and will require a GUI backend.
  - Note: the script drops missing values after constructing the plot; for accurate plotted data consider dropping NA before plotting.


## Common Issues & Troubleshooting

- If `dropna()` appears to have no effect, check that the CSV was parsed into columns (not read as a single object column). Use the diagnostics in `dataPreparation.py` to confirm parsing.
- If numeric columns contain values like `'9 000'` or `'AF'`, convert with `pd.to_numeric(..., errors='coerce')` and then `dropna` to remove non-numeric rows.
- For parser warnings about malformed lines, inspect `data.csv` at the indicated line number to fix quoting or delimiter problems.


## Next steps (optional)

- I can add a `requirements.txt` or `pyproject.toml`.
- I can modify `plottingFunctions.py` to save to a specific file (e.g., `plot.png`) and produce a sample plot.
- I can save the cleaned DataFrame to `cleaned_data.csv` for downstream scripts.

If you'd like any of these, tell me which and I will apply the change.
