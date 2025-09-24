# src/main.py

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from cli import parse_args
from parsers.csv_parser import read_csv_files
from reports.manager import ReportManager
from reports.student_performance import StudentPerformanceReport


def main():
    args = parse_args()

    # Read all CSV files
    data = read_csv_files(args.files)

    # Setup report manager
    manager = ReportManager()
    manager.register_report("student-performance", StudentPerformanceReport())

    # Get and generate report
    report = manager.get_report(args.report)
    if report is None:
        print(f"Unknown report: {args.report}")
        return

    result = report.generate(data)
    print(result)


if __name__ == "__main__":
    main()