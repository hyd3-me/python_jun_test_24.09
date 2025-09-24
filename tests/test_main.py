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

def test_main_empty_csv_files(monkeypatch, tmp_path, capsys):
    """
    Test that main.py handles empty CSV files correctly.
    """
    from src.main import main

    # Create empty CSV files
    file1 = tmp_path / "empty1.csv"
    file1.write_text("student_name,subject,teacher_name,date,grade\n")

    file2 = tmp_path / "empty2.csv"
    file2.write_text("student_name,subject,teacher_name,date,grade\n")

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

    # Check that the report is empty but valid
    output = captured.out
    assert "Student Name" in output
    assert "Average Grade" in output
    # Should only contain header and separators, no data rows
    lines = output.strip().split('\n')
    assert len([line for line in lines if '|' in line]) == 1  # Header only

def test_main_multiple_files_integration(monkeypatch, tmp_path, capsys):
    """
    Test that main.py correctly processes multiple CSV files and calculates average grades.
    """
    from src.main import main

    # Create first CSV file
    file1 = tmp_path / "file1.csv"
    file1.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Иванов Иван,Математика,Петров П.П.,2023-01-01,5\n"
        "Иванов Иван,Физика,Сидоров С.С.,2023-01-02,4\n"
    )

    # Create second CSV file
    file2 = tmp_path / "file2.csv"
    file2.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Петров П.,Химия,Козлова К.К.,2023-01-03,3\n"
        "Иванов Иван,Информатика,Волкова В.В.,2023-01-04,5\n"
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

    output = captured.out

    # Check that both students are present
    assert "Иванов Иван" in output
    assert "Петров П." in output

    # Check that Иванов Иван has average: (5 + 4 + 5) / 3 = 4.67
    assert "4.67" in output

    # Check that Петров П. has average: 3.0
    assert "3.00" in output

    # Check sorting: Иванов (4.67) should come before Петров (3.00)
    lines = output.strip().split('\n')
    student_lines = [line for line in lines if 'Иванов Иван' in line or 'Петров П.' in line]
    assert 'Иванов Иван' in student_lines[0]
    assert 'Петров П.' in student_lines[1]