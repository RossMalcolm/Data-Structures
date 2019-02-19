"""
-------------------------------------------------------
hash_set_array.py
Array version of the Hash Set ADT.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2018-03-22"
-------------------------------------------------------
"""
# Imports
# Use any appropriate data structure here.
from list_array import List
# Define the new_slot slot creation function.
new_slot = List
# Constants
SEP = '-' * 40


class HashSet:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty HashSet of size slots.
        Use: hs = HashSet(slots)
        -------------------------------------------------------
        Precondition:
            size - number of initial slots in hashset (int > 0)
        Postconditions:
            Initializes an empty HashSet.
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []
        
        for i in range(self._slots):
            self._table.append(new_slot())
        self._count = 0
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the hashset.
        Use: n = len( hs )
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the hashset.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the hashset is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the hashset is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot( key )
        -------------------------------------------------------
        Postconditions:
            returns:
            slot - list at the position of hash key in self._slots
        -------------------------------------------------------
        """
        hashkey = hash(key) % self._slots
        slot = self._table[hashkey]
        return slot

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the hashset contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            Returns True if the hashset contains key, False otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        return key in slot

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the hashset, allows only one copy of value.
        Calls _rehash if the hashset _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a comparable data element (?)
        Postconditions:
            returns
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        l = self._find_slot(value)
        
        if value in l:
            inserted = False
            
        else:
            inserted = True
            l.insert(0, value)
            self._count += 1
            
        if self._count > (HashSet._LOAD_FACTOR * self._slots):
            self._rehash()

        return inserted


    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        value = slot.find(key)
        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the hashset, if it exists.
        Use: value = hs.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        x = self._find_slot(key)
        
        if key in x:
            value = x.remove(key)
            self._count -= 1
            
        else:
            value = None

        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the hashset and reallocates the
        existing data within the hashset to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Postconditions:
            Existing data is reallocated amongst the hashset table.
        -------------------------------------------------------
        """
        values = []
        
        for i in range(0, self._slots):
            for item in self._table[i]:
                object = self._table[i].pop(0)
                values.append(object)
             
        amount_of_slots = 2 * self._slots + 1 
        self._slots = 0  
        self._count = 0   
        self._table = []

        for i in range(amount_of_slots):
            self._table.append(new_slot())
            self._slots += 1
         
        for item in values:
            list = self._find_slot(item)
            if item not in list:
                list.insert(0, item)
                self._count += 1
          
            
        return
        

    def debug(self):
        """
        ---------------------------------------------------------
        Prints the contents of the hashset starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Postconditions:
            The contents of the hashset are printed and the slots identified.
        -------------------------------------------------------
        """      
        for i in range(self._slots):
            print("--------------------")
            print("Slot: {}".format(i))
            print()
            
            for j in self._table[i]:
                print(j)
                print()
        print("--------------------")
        

        return
    
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item