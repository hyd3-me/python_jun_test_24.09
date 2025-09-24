# tests/conftest.py

import pytest
from pathlib import Path


@pytest.fixture
def sample_csv_file(tmp_path):
    """
    Create a temporary CSV file with sample data for testing.
    """
    file_path = tmp_path / "sample.csv"
    content = "student_name,subject,teacher_name,date,grade\n"
    file_path.write_text(content)
    return file_path