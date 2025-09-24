# tests/test_main.py

def test_main_integration(monkeypatch, tmp_path, capsys):
    """
    Test that main.py correctly processes CSV files and generates a report.
    """
    from src.main import main

    # Create sample CSV files
    file1 = tmp_path / "students1.csv"
    file1.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5\n"
        "Титов Владислав,География,Орлов Сергей,2023-10-12,4\n"
        "Власова Алина,Биология,Ткаченко Наталья,2023-10-15,5\n"
    )

    file2 = tmp_path / "students2.csv"
    file2.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Иванов Алексей,Математика,Петрова Ольга,2023-09-10,5\n"
        "Петрова Мария,Физика,Сидоров Иван,2023-09-12,4\n"
    )

    # Mock command line arguments
    monkeypatch.setattr('sys.argv', [
        'main.py',
        '--files', str(file1), str(file2),
        '--report', 'student-performance'
    ])

    # Run main
    main()

    # Capture output
    captured = capsys.readouterr()

    # Check that the report contains expected data
    output = captured.out
    assert "Семенова Елена" in output
    assert "Титов Владислав" in output
    assert "Власова Алина" in output
    assert "Иванов Алексей" in output
    assert "Петрова Мария" in output
    assert "5.0" in output  # Average grade for some students

def test_main_unknown_report(monkeypatch, tmp_path, capsys):
    """
    Test that main.py prints an error when an unknown report is requested.
    """
    from src.main import main

    # Create a temporary CSV file
    file1 = tmp_path / "students.csv"
    file1.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Иванов Иван,Математика,Петров П.П.,2023-01-01,5\n"
    )

    # Mock command line arguments with unknown report
    monkeypatch.setattr('sys.argv', [
        'main.py',
        '--files', str(file1),
        '--report', 'unknown-report'
    ])

    # Run main
    main()

    # Capture output
    captured = capsys.readouterr()

    # Check that error message is printed
    assert "Unknown report: unknown-report" in captured.out