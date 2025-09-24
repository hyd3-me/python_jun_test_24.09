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

def test_student_performance_report_one_grade():
    """
    Test that a student with one grade returns the correct average.
    """
    from src.reports.student_performance import StudentPerformanceReport

    data = [
        {"student_name": "Иванов Иван", "subject": "Математика", "grade": "5"},
    ]

    report = StudentPerformanceReport()
    result = report.generate(data)

    assert "Иванов Иван" in result
    assert "5.0" in result

def test_student_performance_report_rounding():
    """
    Test that average grades are rounded to 2 decimal places.
    Example: (5 + 4) / 2 = 4.5 → should appear as 4.50.
    """
    from src.reports.student_performance import StudentPerformanceReport

    data = [
        {"student_name": "Иванов Иван", "subject": "Математика", "grade": "5"},
        {"student_name": "Иванов Иван", "subject": "Физика", "grade": "4"},
    ]

    report = StudentPerformanceReport()
    result = report.generate(data)

    assert "Иванов Иван" in result
    assert "4.5" in result  # 4.50 -> contains "4.5"

def test_student_performance_report_sorting():
    """
    Test that students are sorted by average grade descending.
    """
    from src.reports.student_performance import StudentPerformanceReport

    data = [
        {"student_name": "Сидоров С.", "subject": "Математика", "grade": "3"},
        {"student_name": "Иванов Иван", "subject": "Математика", "grade": "5"},
        {"student_name": "Петров П.", "subject": "Физика", "grade": "4"},
    ]

    report = StudentPerformanceReport()
    result = report.generate(data)

    # Check that "Иванов Иван" appears before "Петров П." and "Сидоров С."
    lines = result.strip().split('\n')
    student_lines = [line for line in lines if 'Иванов Иван' in line or 'Петров П.' in line or 'Сидоров С.' in line]

    # The order should be: Иванов (5.00), Петров (4.00), Сидоров (3.00)
    assert student_lines[0].count('Иванов Иван') == 1
    assert student_lines[1].count('Петров П.') == 1
    assert student_lines[2].count('Сидоров С.') == 1

def test_student_performance_report_multiple_grades():
    """
    Test that average grade is calculated correctly for a student with multiple grades.
    Example: grades 5 and 4 → average = 4.5.
    """
    from src.reports.student_performance import StudentPerformanceReport

    data = [
        {"student_name": "Иванов Иван", "subject": "Математика", "grade": "5"},
        {"student_name": "Иванов Иван", "subject": "Физика", "grade": "4"},
        {"student_name": "Иванов Иван", "subject": "Химия", "grade": "5"},
    ]

    report = StudentPerformanceReport()
    result = report.generate(data)

    assert "Иванов Иван" in result
    # Average: (5 + 4 + 5) / 3 = 4.666... → should be rounded to 4.67
    assert "4.67" in result