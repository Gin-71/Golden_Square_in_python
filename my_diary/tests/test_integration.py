"""
Input / Output diagram

add one entry and check the entries list, type DiaryEntry ==> entries_list
add two entries and check the entries list, type DiaryEntry ==> entries_list

add one entry and count the words ==> numbers of words - int / use count_words from diary_entry
add two entries and count the words ==> numbers of words in both entries together - int / use count_words from diary_entry

add one entry and return the reading time ==> reading time - int / use count_words from diary_entry
add two entries and return the reading time ==> reading time - int / use count_words from diary_entry

add two entries and return the best entry ==> entry - Diary_entry / use count_words from diary_entry

edge cases
empty string ==> Exception "Empty entry is not valid"
wrong format ==> Exception "The entry should be diary_empty type"
"""