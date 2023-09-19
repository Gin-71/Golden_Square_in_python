from lib.report_length import *

def test_report_length_python():
    result = report_length("python")
    assert result == "This string was 6 characters long."
