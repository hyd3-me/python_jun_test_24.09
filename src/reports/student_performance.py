# src/reports/student_performance.py

from typing import List, Dict
from collections import defaultdict
from tabulate import tabulate


class StudentPerformanceReport:
    """
    Generates a report of average grades per student, sorted by average grade descending.
    """

    def generate(self, data: List[Dict]) -> str:
        """
        Generate a table of average grades per student.
        """
        if not data:
            return tabulate([], headers=["Student Name", "Average Grade"], tablefmt="grid")

        grades_by_student = defaultdict(list)

        for row in data:
            student_name = row['student_name']
            grade = int(row['grade'])
            grades_by_student[student_name].append(grade)

        avg_grades = {
            student: round(sum(grades) / len(grades), 2)
            for student, grades in grades_by_student.items()
        }

        sorted_students = sorted(avg_grades.items(), key=lambda x: x[1], reverse=True)

        table = [[name, avg] for name, avg in sorted_students]
        headers = ["Student Name", "Average Grade"]
        return tabulate(table, headers=headers, tablefmt="grid")