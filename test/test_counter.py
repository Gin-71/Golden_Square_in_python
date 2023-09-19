from lib.counter import *

def test_counter_in_cero():
    little_counter = Counter()
    assert little_counter.report() == "Counted to 0 so far."