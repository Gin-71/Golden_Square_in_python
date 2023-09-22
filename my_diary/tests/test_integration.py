import pytest
from lib.diary_entry import *
from lib.diary import *

"""
Input / Output diagram

add one entry and check the entries list, type DiaryEntry ==> entries_list
add two entries and check the entries list, type DiaryEntry ==> entries_list
"""
def test_one_entries_list():
    first_diary = Diary()
    first_entry = DiaryEntry('Friday 22', 'Pairing Session With Hilary')
    first_diary.add(first_entry)
    assert first_diary.all() == [first_entry]

def test_two_entries_list():
    first_diary = Diary()
    first_entry = DiaryEntry('Friday 22', 'Pairing Session With Hilary')
    second_entry = DiaryEntry('Thursday 21', 'Pairing with Catherine')
    first_diary.add(first_entry)
    first_diary.add(second_entry)
    assert first_diary.all() == [first_entry, second_entry]

"""

add one entry and count the words ==> numbers of words - int / use count_words from diary_entry
add two entries and count the words ==> numbers of words in both entries together - int / use count_words from diary_entry
"""
def test_count_words_one_entry():
    first_diary = Diary()
    first_entry = DiaryEntry('Friday 22', 'Pairing Session With Hilary')
    first_diary.add(first_entry)
    assert first_diary.count_words() == 4

def test_count_words_two_entries():
    first_diary = Diary()
    first_entry = DiaryEntry('Friday 22', 'Pairing Session With Hilary')
    second_entry = DiaryEntry('Thursday 21', 'Pairing with Catherine')
    first_diary.add(first_entry)
    first_diary.add(second_entry)
    assert first_diary.count_words() == 7

"""
add one entry and return the reading time ==> reading time - int / use count_words from diary_entry
add two entries and return the reading time ==> reading time - int / use count_words from diary_entry
"""
def test_one_entry_reading_time():
    first_diary = Diary()
    first_entry = DiaryEntry('Friday 22', 'Pairing With Hilary')
    first_diary.add(first_entry)
    assert first_diary.reading_time(3) == 1

def test_two_entries_reading_time():
    first_diary = Diary()
    first_entry = DiaryEntry('Friday 22', 'Pairing Session With Hilary')
    second_entry = DiaryEntry('Thursday 21', 'Pairing with Catherine')
    first_diary.add(first_entry)
    first_diary.add(second_entry)
    assert first_diary.reading_time(2) == 4

"""
add two entries and return the best entry ==> entry - Diary_entry / use count_words from diary_entry
"""
def test_best_entry():
    first_diary = Diary()
    first_entry = DiaryEntry('Friday 22', 'Pairing Session With Hilary')
    second_entry = DiaryEntry('Thursday 21', 'Pairing with Catherine')
    first_diary.add(first_entry)
    first_diary.add(second_entry)
    assert first_diary.find_best_entry_for_reading_time(1, 4) == first_entry

"""
edge cases
empty string ==> Exception "Empty entry is not valid"

"""
def test_empty_contents():
    first_diary = Diary()
    first_entry = DiaryEntry('Friday 22', '')
    with pytest.raises(Exception) as e:
        first_diary.add(first_entry)
    error_message = str(e.value)
    assert error_message == 'Empty contents!'

def test_empty_title():
    first_diary = Diary()
    first_entry = DiaryEntry('', 'Pairing Session With Hilary')
    with pytest.raises(Exception) as e:
        first_diary.add(first_entry)
    error_message = str(e.value)
    assert error_message == 'Empty title!'

def test_empty_entry():
    first_diary = Diary()
    first_entry = DiaryEntry('', '')
    with pytest.raises(Exception) as e:
        first_diary.add(first_entry)
    error_message = str(e.value)
    assert error_message == 'Nothing to add!'

def test_wrong_format():
    first_diary = Diary()
    with pytest.raises(Exception) as e:
        first_diary.add('not correctly')
    error_message = str(e.value)
    assert error_message == 'The entry should be diary_empty type'
"""
wrong format ==> Exception "The entry should be diary_empty type"
"""