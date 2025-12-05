import os
import argparse

# Parse arguments early so we can choose a backend before importing pyplot
parser = argparse.ArgumentParser(description="Create a correlation scatter plot.")
parser.add_argument("--out", help="output filename (default: correlation_plot.png)", default="correlation_plot.png")
parser.add_argument("--no-open", help="do not open/show the image", action="store_true")
parser.add_argument("--no-save", help="do not save the image to disk", action="store_true")
args = parser.parse_args()

import matplotlib
# Try to use an interactive GUI backend when the user intends to open the plot.
interactive_backend = False
if not args.no_open:
	try:
		matplotlib.use("TkAgg")
		interactive_backend = True
	except Exception:
		# fallback to Agg for headless environments
		matplotlib.use("Agg")
else:
	matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV and be tolerant of space-thousands / surrounding spaces
health_data = pd.read_csv(
	"data.csv",
	header=0,
	sep=",",
	thousands=" ",
	skipinitialspace=True,
	na_values=["", "NA", "N/A", "n/a", "NULL"],
)

# Ensure the plotted columns are numeric (remove internal spaces like '9 000')
for col in ["Average_Pulse", "Calorie_Burnage"]:
	if col in health_data.columns:
		health_data[col] = pd.to_numeric(
			health_data[col].astype(str).str.replace(r"\s+", "", regex=True),
			errors="coerce",
		)

# Drop rows where either plotting column is missing after coercion
health_data = health_data.dropna(subset=["Average_Pulse", "Calorie_Burnage"])

# Create scatter plot
fig, ax = plt.subplots()
ax.scatter(health_data["Average_Pulse"], health_data["Calorie_Burnage"])
ax.set_xlabel("Average_Pulse")
ax.set_ylabel("Calorie_Burnage")
plt.tight_layout()

# Show the plot interactively (if requested). After the window is closed,
# prompt the user whether to save the image unless `--no-save` was specified.
shown = False
if not args.no_open:
	try:
		plt.show()
		shown = True
	except Exception:
		# Could not show (headless environment); we'll fall back to saving.
		shown = False

if args.no_save:
	# User explicitly requested not to save; just close the figure.
	plt.close(fig)
else:
	if shown:
		try:
			resp = input(f"Save plot to '{args.out}'? [y/N]: ")
		except Exception:
			resp = ""
		if resp.lower().startswith("y"):
			plt.savefig(args.out)
			print(f"Saved plot to: {args.out}")
	else:
		# Headless or not shown — save automatically
		plt.savefig(args.out)
		print(f"Saved plot to: {args.out}")
	plt.close(fig)
	if not args.no_open and not shown:
		# If we couldn't show the GUI but the user wanted the file opened, try opening it.
		try:
			os.startfile(args.out)
		except Exception:
			pass
