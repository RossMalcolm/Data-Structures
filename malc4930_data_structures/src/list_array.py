
"""
-------------------------------------------------------
list_array.py
Array version of the list ADT.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-19"
-------------------------------------------------------
"""
from copy import deepcopy


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: l = List()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty list.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the list at index i.
        Use: l.insert(i, value)
        -------------------------------------------------------
        Preconditions:
            i - index value (int)
            value - a data element (?)
        Postconditions:
            a copy of value is added to index i, all other values are pushed right
            If i outside of range of length of list, appended to end
        -------------------------------------------------------
        """
        if i+1 > len(self._values):
            self.append(deepcopy(value))
        else:
            new_list=self._values[:i]+ [deepcopy(value)]+ self._values[i:]
            self._values=deepcopy(new_list)
           
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of key in the list, -1 if key is not found (int)
        -------------------------------------------------------
        """
        i = 0
        length = len(self._values)
        
        while i < length and self._values[i] != key:
            i += 1
        
        if i == length:
            i = -1
            
        return i
    
    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of key in the list, -1 if key is not found (int)
        -------------------------------------------------------
        """
        
        if len(self) > 0:
            i = self._linear_search_r_aux(key, 0)
        else:
            i = -1 
        return i
        
        
        
    def _linear_search_r_aux(self, key, index):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of key in the list, -1 if key is not found (int)
        -------------------------------------------------------
        """
        if index >= len(self._values):
            i=-1
        elif self._values[index] == key:
            i = index
        elif self._values[index] != key:
            i = self._linear_search_r_aux(key, index + 1)
        
           
        return i 

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list that matches key.
        Use: value = l.remove(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty list"
        i = self._linear_search(key)
        
        if i == -1:
            value = None
        else:
            value = self._values.pop(i)

        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        i = self._linear_search(key)
        
        if i != -1:
            value = self._values[i]
            
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty list"
        value = self._values[-1]
        
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of the location of key in the list, -1 if
              key is not in the list. (int)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return i

    def _valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._valid_index(i)
        -------------------------------------------------------
        Preconditions:
            i - an index value (int)
        Postconditions:
            returns
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = len(self._values)
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
        Postconditions:
            returns
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._valid_index(i), "Invalid index value"
        value = deepcopy(self._values[i])
        
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
            value - a data value (?)
        Postconditions:
            The i-th element of list contains a copy of value. The existing
                value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._valid_index(i), "Invalid index value"
        self._values[i] = deepcopy(value)
        
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            True if the list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        status = True
        
        i = self._linear_search(key)
        
        if i == -1:
            status = False
        
        return status

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = l.max()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find maximum of an empty list"
        value = self._values[0]
        
        for i in self._values:
            if i > value:
                value = i

        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = l.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find minimum of an empty list"
        value = self._values[0]
        for i in self._values:
            if i < value:
                value = i

        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = l.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        
        number = 0
        for i in self._values:
            if i == key:
                number+=1

        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the operation was called.
        -------------------------------------------------------
        """
        return self._values[::-1]

    def append(self, value):
        """
        ---------------------------------------------------------
        Appends a copy of value to the end of the list.
        Use: l.append(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the end of the list.
        -------------------------------------------------------
        """
        self._values.append(value)
        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list.
        Use: l.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        count = 0
        cleaned = List()
        while count < len(self._values):
            key = self._values[count]
            if key not in cleaned:
                cleaned.append(key)
                count +=1
            elif key in cleaned:
                self._values.pop(count)
                
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = l.pop()
        Use: value = l.pop(i)
        -------------------------------------------------------
        Preconditions:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Postconditions:
            returns
            value - if args exists, the value at position args[0], otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            i = args[0]
            value = self._values.pop(i)
            
        else:
            value = self._values.pop()
            
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            returns
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
    
    def identical(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical, i.e. same values appear
        in the same locations in both lists. (iterative version)
        Use: b = l.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            is_identical - True if this list contains the same values as rs
            in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        is_identical = True
        count = 0
        if len(self._values) != len(rs._values):
            is_identical = False
        else:
            while count < len(self._values):
                if self._values[count] != rs._values[count]:
                    is_identical = False
                count+=1
        return is_identical
    
    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            Removes all values matching key.
        -------------------------------------------------------
        """
        count = 0
        while count < len(self._values):
            if self._values[count] == key:
                self._values.pop(count)
            else:
                count += 1
        return 
    
    def intersection(self, rs):
        """
        -------------------------------------------------------
        Returns a list that contains only values that appear in both
        the current List and rs.
        Use: l2 = 11.intersection(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another List (List)
        Postconditions:
            returns
            new_list - A List that contains only the values found in both
            the current List and rs. Values do not repeat. (List)
        -------------------------------------------------------
        """
        new_list = List()
        for i in self._values:
            for j in rs._values:
                if i == j and j not in new_list:
                    new_list.append(j)
        
        return new_list
    
    def union(self, rs): 
        """
        -------------------------------------------------------
        Returns a list that contains all values in both
        the current List and rs.
        Use: nl = l.union(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            new_list - contains all values found in both the current
            List and rs. Values do not repeat. (List)
        -------------------------------------------------------
        """
        new_list = List()
        for i in self._values:
            if i not in new_list:
                new_list.append(i)
        
        for j in rs._values:
            if j not in new_list:
                new_list.append(j)
        
        return new_list
    
    
    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the list.
        Use: l.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element. (?)
        Postconditions:
            value is added to the front of the list.
        -------------------------------------------------------
        """
        self._values = [value] + self._values
        return
    
    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = l.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty list"
        value = self._values[0]
        self._values.pop(0)

        return value
    
    def combine(self, s2):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(s2)
        -------------------------------------------------------
        Preconditions:
            s2- an array-based List (List)
        Postconditions:
            returns
            new_list - the contents of the current List and s2
                are interlaced into new_list - current List and s2
                are empty (List)
        -------------------------------------------------------
        """
        new_list = List()
        
        while len(self._values) != 0 or not s2.is_empty():
            if len(self._values) != 0:
                new_list.append(self._values.pop(0))
            if len(s2) != 0:
                new_list.append(s2.pop(0))
                
        return new_list
    
    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. ls contains the first half,
        rs the second half. Current list becomes empty.
        Use: ls, rs = l.split()
        -------------------------------------------------------
        Postconditions:
            returns
            ls - a new List with >= 50% of the original List (List)
            rs - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        ls = List()
        rs = List()
        length = len(self._values)-1
        count = 0
        while count <= length:
            if count <= (length//2):
                key = self._values.pop(0)
                ls.append(key)
            elif count > (length//2):
                key = self._values.pop(0)
                rs.append(key)
                
            count = count+1
        return ls, rs
            
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Postconditions:
            returns
            even - the even indexed elements of the list (List)
            odd - the odd indexed elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()
        count = 0 
        while len(self._values) != 0 :
            if (count % 2) == 0:
                even.append(self._values.pop(0))
            elif (count % 2) != 0:
                odd.append(self._values.pop(0))
            
            count +=1
        return even, odd
    
    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. ls contains all the values 
        where the result of calling func(value) is True, 
        rs contains the remaining values.
        Use: ls, rs = l.split_apply(func)
        -------------------------------------------------------
        Preconditions:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns false.
        Postconditions:
            returns
            ls - a new List with values where func(value) is True (List)
            rs - a new List with values where func(value) is False (List)
            self is empty. Order of values is new lists is maintained.
        -------------------------------------------------------
        """
        ls = List()
        rs = List()
        
        while len(self._values) > 0:
            if func(self._values[0]) is True:
                ls.append(self._values.pop(0))
            else:
                rs.append(self._values.pop(0))
        return ls, rs
    

    
    
                
            
            
        