"""
-------------------------------------------------------
morse.py
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
Morse Code functions and data.
-------------------------------------------------------
Data Definitions
-------------------------------------------------------
"""
# In order by letters.
data1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..--'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))

# In order by splitting.
data2 = (('M', '--'), ('F', '..-.'), ('T', '-'),
         ('C', '-.-.'), ('J', '.---'), ('P', '.--.'),
         ('W', '.--'), ('A', '.-'), ('D', '-..'),
         ('H', '....'), ('K', '-.-'), ('N', '-.'),
         ('R', '.-.'), ('U', '..--'), ('Y', '-.--'),
         ('B', '-...'), ('E', '.'), ('I', '..'),
         ('G', '--.'), ('L', '.-..'), ('O', '---'),
         ('Q', '--.-'), ('S', '...'), ('V', '...-'),
         ('X', '-..-'), ('Z', '--..'))

# In order by popularity.
data3 = (('E', '.'), ('T', '-'), ('A', '.-'),
         ('O', '---'), ('I', '..'), ('N', '-.'),
         ('S', '...'), ('H', '....'), ('R', '.-.'),
         ('D', '-..'), ('L', '.-..'), ('U', '..--'),
         ('C', '-.-.'), ('M', '--'), ('P', '.--.'),
         ('F', '..-.'), ('Y', '-.--'), ('W', '.--'),
         ('G', '--.'), ('B', '-...'), ('V', '...-'),
         ('K', '-.-'), ('J', '.---'), ('X', '-..-'),
         ('Z', '--..'), ('Q', '--.-'))


class ByLetter:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by letter attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByLetter object.
        Use: var = ByLetter(letter, code)
        -------------------------------------------------------
        Preconditions:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Postconditions:
            ByLetter values are set.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code
        return

    def __eq__(self, rs):
        """
        -------------------------------------------------------
        Compares this ByLetter against another ByLetter for equality.
        Object are equal if their letters match.
        Use: v1 == v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByLetter to compare to (ByLetter)
        Postconditions:
            returns
            result - True if letters match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.letter) == (rs.letter)
        
        return result
        
        

    def __lt__(self, rs):
        """
        -------------------------------------------------------
        Determines if this ByLetter comes before another.
        Use: v1 < v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByLetter to compare to (ByLetter)
        Postconditions:
            returns
            result - True if this ByLetter precedes rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        
        return (self.letter) < (rs.letter)




    def __le__(self, rs):
        """
        -------------------------------------------------------
        Determines if this ByLetter precedes or is or equal to another.
        Use: v1 <= v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByLetter to compare to (ByLetter)
        Postconditions:
            returns
            result - True if this ByLetter precedes or is equal to rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        
        return (self.letter) <= (rs.letter)


    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByLetter data.
        Use: print(v)
        Use: string = str(v)
        -------------------------------------------------------
        Postconditions:
            returns
            string - the formatted contents of ByLetter (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.letter, self.code)
    

class ByCode:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by code attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByCode object.
        Use: var = ByCode(letter, code)
        -------------------------------------------------------
        Preconditions:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Postconditions:
            ByCode values are set.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code
        return

    def __eq__(self, rs):
        """
        -------------------------------------------------------
        Compares this ByCode against another ByCode for equality.
        Object are equal if their codes match.
        Use: v1 == v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByCode to compare to (ByCode)
        Postconditions:
            returns
            result - True if codes match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.code) == (rs.code)
        
        return result

    def __lt__(self, rs):
        """
        -------------------------------------------------------
        Determines if this ByCode comes before another.
        Use: v1 < v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByCode to compare to (ByCode)
        Postconditions:
            returns
            result - True if this ByCode precedes rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        
        return self.code < rs.code

    def __le__(self, rs):
        """
        -------------------------------------------------------
        Determines if this ByCode precedes or is or equal to another.
        Use: v1 <= v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByCode to compare to (ByCode)
        Postconditions:
            returns
            result - True if this ByCode precedes or is equal to rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        
        return self.code <= rs.code

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByCode data.
        Use: print(v)
        Use: string = str(v)
        -------------------------------------------------------
        Postconditions:
            returns
            string - the formatted contents of ByCode (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.code, self.letter)