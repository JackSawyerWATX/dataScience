import os
import sys
import argparse
import subprocess
from pathlib import Path


def discover_scripts(folder: Path):
	"""Return a sorted list of runnable .py scripts in folder, excluding this runner and common non-scripts."""
	exclude = {"main.py", "README.md", "requirements.txt"}
	scripts = []
	for p in folder.iterdir():
		if p.is_file() and p.suffix == ".py" and p.name not in exclude:
			# skip helper files and dunders
			if p.name.startswith("_"):
				continue
			scripts.append(p)
	scripts.sort(key=lambda p: p.name.lower())
	return scripts


def run_script(p: Path, python_exe: str, capture: bool = False):
	cmd = [python_exe, str(p)]
	print(f"\n--- Running: {p.name} ---")
	try:
		if capture:
			res = subprocess.run(cmd, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
			print(res.stdout)
		else:
			res = subprocess.run(cmd, check=False)
		return res.returncode
	except Exception as e:
		print(f"Error running {p.name}: {e}")
		return 1


def main():
	parser = argparse.ArgumentParser(description="Run all example scripts in the dataScience folder.")
	parser.add_argument("--list", action="store_true", help="list discovered scripts and exit")
	parser.add_argument("--yes", "-y", action="store_true", help="do not prompt before running scripts")
	parser.add_argument("--filter", "-f", help="only run scripts containing this substring in filename")
	parser.add_argument("--capture", action="store_true", help="capture stdout/stderr and print after each script")
	args = parser.parse_args()

	folder = Path(__file__).resolve().parent
	scripts = discover_scripts(folder)
	if args.filter:
		scripts = [p for p in scripts if args.filter.lower() in p.name.lower()]

	if args.list:
		print("Discovered scripts:")
		for p in scripts:
			print(" -", p.name)
		return

	if not scripts:
		print("No scripts found to run.")
		return

	print("Scripts to run:")
	for p in scripts:
		print(" -", p.name)

	if not args.yes:
		try:
			resp = input("Proceed to run these scripts sequentially? [y/N]: ")
		except Exception:
			resp = "n"
		if not resp.lower().startswith("y"):
			print("Aborted by user.")
			return

	python_exe = sys.executable or "python"
	failures = []
	for p in scripts:
		code = run_script(p, python_exe, capture=args.capture)
		if code != 0:
			failures.append((p.name, code))

	print("\nAll done.")
	if failures:
		print("Some scripts failed:")
		for name, code in failures:
			print(f" - {name}: exit code {code}")


if __name__ == "__main__":
	main()

