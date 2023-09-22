class GrammarStats:
    def __init__(self):
        self.checks = []
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if (text[0] == text.upper()[0]) and (text[-1] == "."):
            self.checks.append(True)
            return True
        self.checks.append(False)
        return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        counter_True = self.checks.count(True)
        return int((100 * counter_True) / len(self.checks))


        