# Three lines to prefer an interactive backend when available (so plt.show() works).
import sys
import os
import matplotlib
# Only force the non-interactive 'Agg' backend if there is no display (headless)
if os.name != 'nt' and not os.environ.get('DISPLAY'):
	matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

Drowning_Accident = [20,40,60,80,100,120,140,160,180,200]
Ice_Cream_Sale = [20,40,60,80,100,120,140,160,180,200]
Drowning = {"Drowning_Accident": [20,40,60,80,100,120,140,160,180,200],
"Ice_Cream_Sale": [20,40,60,80,100,120,140,160,180,200]}
Drowning = pd.DataFrame(data=Drowning)

Drowning.plot(x="Ice_Cream_Sale", y="Drowning_Accident", kind="scatter")

# Only call plt.show() for interactive backends to avoid native GUI crashes in
# headless or incompatible environments.
import matplotlib as _mpl
backend = _mpl.get_backend().lower()
interactive_backends = ("tk", "qt", "wx", "gtk", "macosx")
if any(k in backend for k in interactive_backends):
	try:
		# block=True so the user sees the window and can close it before the prompt
		plt.show()
	except Exception as e:
		print("Interactive display failed:", e)
else:
	# non-interactive backend (Agg etc.) — do not call show
	print(f"Non-interactive backend '{backend}' in use; skipping plt.show().")

# Compute and print correlation matrix
correlation_beach = Drowning.corr()
print(correlation_beach)

# Prompt the user before saving the plot (yes saves, no does not)
try:
	ans = input("Save plot to 'correlation_vs_causality.png'? (y/n): ").strip().lower()
except Exception:
	ans = "n"

if ans in ("y", "yes"):
	out_file = "correlation_vs_causality.png"
	plt.savefig(out_file, bbox_inches="tight")
	print(f"Saved {out_file}")
else:
	print("Plot not saved.")

plt.close()