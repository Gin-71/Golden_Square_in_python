from lib.password_checker import *
import pytest

def test_password_checker_for_valid_password():
    test_password = PasswordChecker()
    result = test_password.check('12345678')
    assert result == True

def test_password_checker_for_password_shorter_than_8():
    test_password = PasswordChecker()
    with pytest.raises(Exception) as e:
        test_password.check('1234')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."