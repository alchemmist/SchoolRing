#!/usr/bin/python

from pathlib import Path
import subprocess

UI_DIR = Path("assets/ui")
OUTPUT_DIR = Path("schoolring/ui")

def convert_ui_files():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for ui_file in UI_DIR.glob("*.ui"):
        output_file = OUTPUT_DIR / f"{ui_file.stem}_ui.py"
        command = ["pyuic6", str(ui_file), "-o", str(output_file)]
        subprocess.run(command)
        print(f"Converted: {ui_file} -> {output_file}")

if __name__ == "__main__":
    convert_ui_files()

