"""
-------------------------------------------------------
number.py
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
"""


class Number:
    """
    -------------------------------------------------------
    Wraps a class definition around integers.
    Uses class attribute 'comparisons' to determine how many times 
    comparison functions are called on the class.
    Use: print(Number.comparisons)
    Use: Number.comparisons = 0
    -------------------------------------------------------
    """
    comparisons = 0

    def __init__(self, data):
        """
        -------------------------------------------------------
        Creates a Number object.
        -------------------------------------------------------
        Preconditions:
            data - an integer (int)
        Postconditions:
            A Number object containing data is initialized.
        -------------------------------------------------------
        """
        self.data = data
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of Number data.
        -------------------------------------------------------
        Postconditions:
          returns:
          the formatted contents of data (str)
        -------------------------------------------------------
        """
        return str(self.data)

    def __eq__(self, rs):
        """
        -------------------------------------------------------
        Compares this Number against another Number for equality.
        Use: n1 == n2
        -------------------------------------------------------
        Preconditions:
          rs - [right hand side] Number to compare to (Number)
        Postconditions:
          returns:
          result - True if data matches, False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self.data == rs.data
        return result

    def __lt__(self, rs):
        """
        -------------------------------------------------------
        Determines if this Number comes before another.
        Use: n1 < n2
        -------------------------------------------------------
        Preconditions:
          rs - [right hand side] Number to compare to (Number)
        Postconditions:
          returns:
          result - True if this Number precedes rs,
          False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self.data < rs.data
        return result

    def __le__(self, rs):
        """
        -------------------------------------------------------
        Determines if this Number precedes or is or equal to another.
        Use: n1 <= n2
        -------------------------------------------------------
        Preconditions:
          rs - [right hand side] Number to compare to (movie)
        Postconditions:
          returns:
          result - True if this Number precedes or is equal to rs,
          False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self.data <= rs.data
        return result