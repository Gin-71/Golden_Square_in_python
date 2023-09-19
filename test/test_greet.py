from lib.greet import *

def test_hello_gina():
    result = greet('Gina')
    assert result == "Hello, Gina"