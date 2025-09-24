# tests/test_reports/test_manager.py

def test_report_manager_register_and_get():
    """
    Test that reports can be registered and retrieved by name.
    """
    from src.reports.manager import ReportManager
    from src.reports.student_performance import StudentPerformanceReport

    manager = ReportManager()
    report = StudentPerformanceReport()
    manager.register_report("student-performance", report)

    retrieved = manager.get_report("student-performance")
    assert retrieved is report
    assert isinstance(retrieved, StudentPerformanceReport)