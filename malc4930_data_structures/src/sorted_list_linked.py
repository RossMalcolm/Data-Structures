"""
-------------------------------------------------------
sorted_list_linked.py
Linked version of the SortedList ADT.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-02-24"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SLNode:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SLNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            next_ - another sorted list node (_ListNode)
        Postconditions:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = next_
        return


class SortedList:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty sorted list.
        Use: sl = SortedList()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty sorted list.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

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
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        previous = None
        curr = self._front
      
        while curr is not None and value > curr._data:
            previous = curr
            curr = curr._next
            
        n = _SLNode(value, curr)
        
        if previous is not None:
            previous._next = n

        else:
            
            self._front = n
            
        return
        

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        index = 0
        
        while current is not None and current._data < key:
            previous = current
            current = current._next
            index+=1
        
        if current is None or current._data != key:
            index = -1

        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        
        current = self._front
        previous = None
        
        while current is not None and current._data < key:
            previous = current
            current = current._next

        if current is not None and current._data == key:
            value = current._data
            
            if previous is None:
                self._front = self._front._next 
                
            else:
                previous._next = current._next
                
            self._count -=1
            
        else:
            value = None

        return value


    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find in an empty list"
        
        _,current,_ = self._linear_search(key)
        
        if current is None:
            value = None
        else:
            value = deepcopy(current._data)
        
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
        assert self._front is not None, "Cannot peek at an empty list"
        
        value = self._front._data
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _,_,i = self._linear_search(key)

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
        n = self._count
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
        number = 0
        current = self._front
        while number != i:
            current = current._next
            number +=1
        
        value = current._data

        return value

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
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _,_,i = self._linear_search(key)

        return i != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        
        current = self._front
        while current._next is not None:
            current = current._next
        
        value = current._data

        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        value = self._front._data

        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            returns
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        current = self._front
        number = 0
        
        while current is not None:
            if current._data == key:
                number += 1
            current = current._next
        return number

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        duplicates = []
        previous = None
        current = self._front
      
        while current is not None: 
            if current._data not in duplicates:
                duplicates.append(deepcopy(current._data))
                previous = current
                      
            else:
                previous._next = current._next
                self._count = self._count - 1
                
            current = current._next            

        return

    def pop(self, *i):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = l.remove(i)
        -------------------------------------------------------
        Preconditions:
            i - an array of arguments (?)
                i[0], if it exists, is the index
        Postconditions:
            returns
            value - if i exists, the value at position i, otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(i) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(i) == 1:

            if i[0] < 0:
                # index is negative
                i[0] = self._count + i[0]
            j = 0

            while j < i[0]:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._data

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (SortedList)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (SortedList)
        -------------------------------------------------------
        """
        new_list = SortedList()
        current = self._front
        
        while current is not None:
            if current._data in rs and current._data not in new_list:
                node = _SLNode(current._data, None)
                if new_list._count == 0:
                    new_list._front = node
                    current_new = node
                    new_list._count = 1
                else:
                    current_new = node
                    current_new._next = node
                    new_list._count += 1
                    
            current = current._next
            
              
        return new_list

    def union(self, rs):
        """
        -------------------------------------------------------
        Copies all of the values in both self and rs to
        a new List. Each value appears only once. (iterative)
        -------------------------------------------------------
        Preconditions:
            rs - another List (SortedList)
        Postconditions:
            Returns:
            new_list - a List containing one copy each of all values
            in both self and rs. (SortedList)
        -------------------------------------------------------
        """
        new_list = SortedList()
        
        while self._front is not None and rs._front is not None:
            if self._front._data < rs._front._data:
                temp = self._front._data
                self.remove_front()
                
                if temp not in new_list:
                    node = _SLNode(temp, None)
                    
                    if new_list._count == 0:
                        new_list._front = node
                        current_new = node
                        new_list._count = 1
                        
                    else:
                        current_new._next = node
                        current_new = node
                        new_list._count += 1
                        
                
    
                
            else:
                temp = rs._front._data
                rs.remove_front()
                
                if temp not in new_list:
                    node = _SLNode(temp, None)
                    
                    if new_list._count == 0:
                        new_list._front = node
                        current_new = new_list._front
                        new_list._count = 1
                        
                    else:
                        current_new._next = node
                        current_new = node
                        new_list._count += 1
                
        while self._front is not None:
            temp = self._front._data
            self.remove_front()
            
            if temp not in new_list:
                node = _SLNode(temp, None)
                
                if new_list._count == 0:
                    new_list._front = node
                    current_new = new_list._front
                    new_list._count = 1
                    
                else:
                    current_new._next = node
                    current_new = node
                    new_list._count +=1
        
        while rs._front is not None:
            temp = rs._front._data
            rs.remove_front()
            
            if temp not in new_list:
                node = _SLNode(temp, None)
                
                if new_list._count == 0:
                    new_list._front = node
                    current_new = new_list._front
                    new_list._count = 1
                    
                else:
                    current_new._next = node
                    current_new = node
                    new_list._count += 1

        return new_list

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes first node in list.
        Use: value = sl.remove_front()
        -------------------------------------------------------
        Postconditions:
          Returns:
          value - the first value in the list, None if the list is empty.
        -------------------------------------------------------
        """
        if self._front is not None:
            value = self._front
            self._front = self._front._next
            self._count -= 1
        else:
            value = None
        
        return value

    def _reverse(self):
        """
        -------------------------------------------------------
        Helper method - reverses the order of the elements in list.
        Use: l._reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        new_front = None

        while self._front is not None:
            temp = self._front._next
            self._front._next = new_front
            new_front = self._front
            self._front = temp

        self._front = new_front
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next