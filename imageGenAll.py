#!/usr/bin/env python3
# generate_all_course1_images.py
# Auto-discovers and runs all generate_images_part*.py scripts.

import os
import sys
import subprocess
import re
from pathlib import Path

def natural_sort_key(filename):
    """Sort filenames with numbers in natural order: part1, part2, ..., part10"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', filename)]

def main():
    print("🚀 Auto-running all imagegen*.py scripts...\n")
    
    # Get current directory
    cwd = Path(".")
    
    # Find all matching scripts
    part_scripts = sorted(
        (f.name for f in cwd.glob("imagegen*.py")),
        key=natural_sort_key
    )
    
    if not part_scripts:
        print("❌ No scripts matching 'generate_images_part*.py' found.")
        sys.exit(1)
    
    print(f"▶️  Found {len(part_scripts)} script(s):")
    for s in part_scripts:
        print(f"    - {s}")
    print()

    # Ensure output folder exists
    (cwd / "images").mkdir(exist_ok=True)

    # Run each script
    for script in part_scripts:
        print(f"──────────────────────────────")
        print(f"▶️  Running: {script}")
        print(f"──────────────────────────────")
        result = subprocess.run([sys.executable, script])
        if result.returncode != 0:
            print(f"❌ FAILED on {script}. Stopping.")
            sys.exit(1)

    # Final summary
    png_count = len(list((cwd / "images").glob("*.png")))
    print("\n" + "="*50)
    print(f"🎉 Done! Total PNG files: {png_count}")
    print("="*50)

if __name__ == "__main__":
    main()