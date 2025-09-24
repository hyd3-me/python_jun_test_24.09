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