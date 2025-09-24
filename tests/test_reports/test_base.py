# tests/test_reports/test_base.py
import pytest

def test_base_report_is_abstract():
    """
    Test that BaseReport cannot be instantiated directly.
    """
    from src.reports.base import BaseReport

    with pytest.raises(TypeError):
        BaseReport()