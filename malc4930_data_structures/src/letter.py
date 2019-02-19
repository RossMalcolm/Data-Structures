"""
-------------------------------------------------------
Letter.py
Stores a single letter of the alphabet, and counts occurrences and
comparisons when the letter is used.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2018-03-09"
-------------------------------------------------------
"""


class Letter:

    def __init__(self, letter):
        """
        -------------------------------------------------------
        Initialize a Letter object.
        Use: l = Letter(char)
        -------------------------------------------------------
        Preconditions:
            letter - an single uppercase letter of the alphabet (str)
        Postconditions:
            Letter values are set.
        -------------------------------------------------------
        """
        assert letter.isalpha() and letter.isupper(), "Invalid letter"

        self.letter = letter
        self.count = 0
        self.comparisons = 0
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of Letter data.
        Use: print(m)
        Use: s = str(m)
        -------------------------------------------------------
        Postconditions:
            returns:
            the value of self.letter (str)
        -------------------------------------------------------
        """
        return "{}: {}, {}".format(self.letter, self.count, self.comparisons)

    def __eq__(self, rs):
        """
        -------------------------------------------------------
        Compares this Letter against another Letter for equality.
        Use: l == rs
        -------------------------------------------------------
        Preconditions:
            rs - [right side] Letter to compare to (Letter)
        Postconditions:
            returns:
            result - True if name and origin match, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.count += 1
        self.comparisons += 1
        result = self.letter == rs.letter
        return result

    def __lt__(self, rs):
        """
        -------------------------------------------------------
        Determines if this Letter comes before another.
        Use: f < rs
        -------------------------------------------------------
        Preconditions:
            rs - [right side] Letter to compare to (Letter)
        Postconditions:
            returns:
            result - True if Letter precedes rs, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        result = self.letter < rs.letter
        return result

    def __le__(self, rs):
        """
        -------------------------------------------------------
        Determines if this Letter precedes or is or equal to another.
        Use: f <= rs
        -------------------------------------------------------
        Preconditions:
            rs - [right side] Letter to compare to (Letter)
        Postconditions:
            returns:
            result - True if this Letter precedes or is equal to rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        result = self.letter <= rs.letter
        return result