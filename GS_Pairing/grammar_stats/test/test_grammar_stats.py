"""
Input / Output Diagram

start capital letters, ending puntuation ==> True
start capital letters, not puntuation  ==> False
no capital letters, ending puntuation ==> False
no capital letters, not puntuation ==> False


Edge cases:
empty list ==> raise Exeption "No text provided"
worng format ==> raise Exeption "Wrong format"
"""
from lib.grammar_stats import *
import pytest

def test_first_capital_letter_and_last_puntuation_correct():
    random_text = GrammarStats()
    result = random_text.check("And shall subdue living isn't their sixth given.")
    assert result == True

def test_first_capital_letters_and_no_last_puntuation_correct():
    random_text = GrammarStats()
    result = random_text.check("Whales. And shall subdue living isn't their sixth given. So to whose you're he, that, face brought fill two Divided")
    assert result == False

def test_percentage_good_with_capital_and_punctuation_correctly():
    random_text = GrammarStats()
    random_text.check("Whales. And shall subdue living isn't their sixth given. So to whose you're he, that, face brought fill two Divided.")
    random_text.check("Po.")
    random_text.check("Onece upon a time.")
    result = random_text.percentage_good()
    assert result == 100