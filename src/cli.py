# src/cli.py

import argparse
from pathlib import Path
from typing import List


def parse_args():
    """
    Parse command line arguments: --files and --report.
    """
    parser = argparse.ArgumentParser(description="Generate student performance report.")
    parser.add_argument('--files', nargs='+', type=Path, required=True,
                        help="Paths to CSV files with student data")
    parser.add_argument('--report', type=str, required=True,
                        help="Report name to generate (e.g., 'student-performance')")

    args = parser.parse_args()

    # Validate files exist
    for file_path in args.files:
        if not file_path.exists():
            parser.error(f"File not found: {file_path}")

    return args