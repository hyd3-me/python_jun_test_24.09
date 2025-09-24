# tests/test_cli.py

def test_parse_args_success(monkeypatch, sample_csv_file):
    """
    Test that valid --files and --report arguments are parsed correctly.
    """
    # Use fixture to get the file
    file1 = sample_csv_file

    # Mock sys.argv to simulate command line input
    monkeypatch.setattr('sys.argv', [
        'main.py',
        '--files', str(file1),
        '--report', 'student-performance'
    ])

    # Import here to avoid side effects during test collection
    from src.cli import parse_args

    args = parse_args()
    assert len(args.files) == 1
    assert str(args.files[0]) == str(file1)
    assert args.report == 'student-performance'