# tests/test_csv_parser.py

def test_read_csv_files_success(sample_csv_file):
    """
    Test that CSV files are read and combined correctly.
    """
    from src.parsers.csv_parser import read_csv_files

    result = read_csv_files([sample_csv_file])
    assert len(result) == 0  # Because the file is empty except for headers

    # Add some data to the file
    sample_csv_file.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Иванов Иван,Математика,Петров П.П.,2023-01-01,5\n"
    )

    result = read_csv_files([sample_csv_file])
    assert len(result) == 1
    assert result[0]['student_name'] == 'Иванов Иван'
    assert result[0]['grade'] == '5'

def test_read_csv_files_two_files(tmp_path):
    """
    Test that two CSV files are read and combined correctly.
    """
    from src.parsers.csv_parser import read_csv_files

    file1 = tmp_path / "file1.csv"
    file1.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Иванов Иван,Математика,Петров П.П.,2023-01-01,5\n"
    )

    file2 = tmp_path / "file2.csv"
    file2.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Сидоров С.С.,Физика,Козлова А.Б.,2023-01-02,4\n"
    )

    result = read_csv_files([file1, file2])
    assert len(result) == 2
    assert result[0]['student_name'] == 'Иванов Иван'
    assert result[1]['student_name'] == 'Сидоров С.С.'

def test_read_csv_files_empty_file(tmp_path):
    """
    Test that reading an empty CSV file returns an empty list.
    """
    from src.parsers.csv_parser import read_csv_files

    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")  # Just empty

    result = read_csv_files([empty_file])
    assert result == []