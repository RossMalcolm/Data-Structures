
"""
-------------------------------------------------------
word.py
Stores a single word and counts occurrences and
comparisons when the word is used.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2018-03-22"
-------------------------------------------------------
"""


class Word:

    def __init__(self, word):
        """
        -------------------------------------------------------
        Initialize a Word object.
        Use: l = Word(char)
        -------------------------------------------------------
        Preconditions:
            word - an single lowercase word of the alphabet (str)
        Postconditions:
            Word values are set.
        -------------------------------------------------------
        """
        assert word.isalpha() and word.islower(), "Invalid word"

        self.word = word
        self.comparisons = 0
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of Word data.
        Use: print(m)
        Use: s = str(m)
        -------------------------------------------------------
        Postconditions:
            returns:
            the value of self.word (str)
        -------------------------------------------------------
        """
        return "{}: {:,d}".format(self.word, self.comparisons)

    def __eq__(self, rs):
        """
        -------------------------------------------------------
        Compares this Word against another Word for equality.
        Use: l == rs
        -------------------------------------------------------
        Preconditions:
            rs - [right side] Word to compare to (Word)
        Postconditions:
            returns:
            result - True if name and origin match, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        result = self.word == rs.word
        return result

    def __lt__(self, rs):
        """
        -------------------------------------------------------
        Determines if this Word comes before another.
        Use: f < rs
        -------------------------------------------------------
        Preconditions:
            rs - [right side] Word to compare to (Word)
        Postconditions:
            returns:
            result - True if Word precedes rs, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        result = self.word < rs.word
        return result

    def __le__(self, rs):
        """
        -------------------------------------------------------
        Determines if this Word precedes or is or equal to another.
        Use: f <= rs
        -------------------------------------------------------
        Preconditions:
            rs - [right side] Word to compare to (Word)
        Postconditions:
            returns:
            result - True if this Word precedes or is equal to rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        result = self.word <= rs.word
        return result

    def __hash__(self):
        """
        -------------------------------------------------------
        Generates a hash value from a word.
        Use: h = hash(word)
        -------------------------------------------------------
        Postconditions:
            returns
            value - the total of the characters in the name string
                multiplied by the year (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.word:
            value += ord(c)
        return value