"""
Input / Output diagram

count words of the contents ==> quantity of words - int / it could be call by Diary


"""
from lib.diary_entry import *

def test_count_contents_words():
    mydiary = DiaryEntry("Tuesday 17th", "I decided to dye my hair, and it looks fabulous.")
    result = mydiary.count_words()
    assert result == 10

def test_contents_reading_time():
    mydiary = DiaryEntry("Tuesday 17th", "I decided to dye my hair, and it looks fabulous. Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it Today I decided to dye my hair, and it looks fabulous. Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it ")
#    mydiary.format()
    mydiary.count_words()
    result = mydiary.reading_time(200)
    assert result == 1

def test_contents_reading_chunk():
    mydiary = DiaryEntry("Tuesday 17th", "I decided to dye my hair, and it looks fabulous. Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it Today I decided to dye my hair, and it looks fabulous. Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it ")
    result = mydiary.reading_chunk(2, 5)
    assert result == "I decided to dye my hair, and it looks fabulous."

def test_contents_reading_chunk_several_times():
    mydiary = DiaryEntry("Tuesday 17th", "I decided to dye my hair, and it looks fabulous. Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it Today I decided to dye my hair, and it looks fabulous. Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it looks fabulous.Today I decided to dye my hair, and it ")
    mydiary.reading_chunk(2, 1)
    mydiary.reading_chunk(2, 1)
    mydiary.reading_chunk(2, 1)
    result = mydiary.reading_chunk(2, 1) 
    assert result == "and it"