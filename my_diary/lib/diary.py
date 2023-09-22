from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self.the_list = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        if type(entry) != DiaryEntry:
            raise Exception('The entry should be diary_empty type')
        elif entry.contents == '' and entry.title == '':
            raise Exception('Nothing to add!')
        elif entry.contents == '':
            raise Exception('Empty contents!')
        elif entry.title == '':
            raise Exception('Empty title!')
        else:
            self.the_list.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.the_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        counter = 0
        for entry in self.the_list:
            counter += entry.count_words()
        return counter

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        words = self.count_words()
        if words % wpm == 0:
            return int(words / wpm)
        else:
            return int(words / wpm) + 1

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        entry_words = 0
        my_favourite_entry = ''
        words = wpm * minutes
        for entry in self.the_list:
            if entry.count_words() <= words and entry.count_words() > entry_words:
                my_favourite_entry = entry
                entry_words = entry.count_words()
        return my_favourite_entry