# tests/test_reports/test_student_performance.py

def test_student_performance_report_single_student():
    """
    Test that average grade is calculated correctly for a single student with multiple grades.
    """
    from src.reports.student_performance import StudentPerformanceReport

    data = [
        {"student_name": "Иванов Иван", "subject": "Математика", "grade": "5"},
        {"student_name": "Иванов Иван", "subject": "Физика", "grade": "4"},
    ]

    report = StudentPerformanceReport()
    result = report.generate(data)

    assert "Иванов Иван" in result
    assert "4.5" in result

def test_student_performance_report_empty_data():
    """
    Test that an empty data list returns an empty table.
    """
    from src.reports.student_performance import StudentPerformanceReport

    report = StudentPerformanceReport()
    result = report.generate([])
    
    assert "Student Name" in result
    assert "Average Grade" in result
    assert len(result.strip().split('\n')) == 4  # Header + separator + empty row + separator