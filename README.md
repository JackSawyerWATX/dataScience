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


## Common Issues & Troubleshooting

- If `dropna()` appears to have no effect, check that the CSV was parsed into columns (not read as a single object column). Use the diagnostics in `dataPreparation.py` to confirm parsing.
- If numeric columns contain values like `'9 000'` or `'AF'`, convert with `pd.to_numeric(..., errors='coerce')` and then `dropna` to remove non-numeric rows.
- For parser warnings about malformed lines, inspect `data.csv` at the indicated line number to fix quoting or delimiter problems.


## Next steps (optional)

- I can add a `requirements.txt` or `pyproject.toml`.
- I can modify `plottingFunctions.py` to save to a specific file (e.g., `plot.png`) and produce a sample plot.
- I can save the cleaned DataFrame to `cleaned_data.csv` for downstream scripts.

If you'd like any of these, tell me which and I will apply the change.
