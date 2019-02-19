"""
-------------------------------------------------------
deque_linked_new.py
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-07-08"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy

class _DequeNode:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque_linked_new node.
        Use: node = _dequeNode(value, prev, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            _prev - another deque_linked_new node (_DequeNode)
            _next - another deque_linked_new node (_DequeNode)
        Postconditions:
            Initializes a deque_linked_new node that contains a copy of value
            and links to the previous and next nodes in the deque_linked_new.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._prev = _prev
        self._next = _next
        return


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque_linked_new.
        Use: d = deque_linked_new()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty deque_linked_new.
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque_linked_new is empty.
        Use: b = d.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if the deque_linked_new is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque_linked_new.
        Use: n = len(d)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of values in the deque_linked_new.
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque_linked_new.
        Use: d.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the front of the deque_linked_new.
        -------------------------------------------------------
        """
        node = _DequeNode(value, None, self._front)
        
        if self._count == 0:
            self._front = node
            self._rear = node
        
        else:
            self._front._prev = node
            self._front = node
        
        self._count += 1

        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque_linked_new.
        Use: d.insert_rear(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the deque_linked_new.
        -------------------------------------------------------
        """
        node = _DequeNode(value, self._rear, None )
        
        if self._count == 0:
            self._front = node
            self._rear = node
        else:
            self._rear._next = node
            self._rear = node
        
        self._count += 1

        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque_linked_new.
        Use: v = d.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of deque_linked_new - the value is
                removed from deque_linked_new.
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty dequeue"
    
        value = self._front._data
        
        if self._count == 1:
            self._front = None
            self._rear = None
            
        else:
            self._front = self._front._next
            self._front._prev = None
        
        self._count -= 1

        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque_linked_new.
        Use: v = d.remove_rear()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the rear of deque_linked_new - the value is
                removed from deque_linked_new.
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty dequeue"
        
        value = self._rear._data
        
        if self._count == 1:
            
            self._front = None
            
            self._rear = None
        
        else:
            
            self._rear = self._rear._prev
            
            self._rear._next = None
        
        self._count -= 1

        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque_linked_new.
        Use: v = d.peek_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of deque_linked_new -
                the value is not removed from deque_linked_new (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty dequeue"
        
        value = deepcopy(self._front._data)

        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque_linked_new.
        Use: v = d.peek_rear()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the rear of deque_linked_new -
                the value is not removed from deque_linked_new (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty dequeue"
        
        value = deepcopy(self._rear._data)
        
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque_linked_new.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Preconditions:
            l - a pointer to a deque_linked_new node (_DequeNode)
            r - a pointer to a deque_linked_new node (_DequeNode)
        Postconditions:
            l has taken the place of r, r has taken the place of l and
            _front and _rear are updated as appropriate
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
    
        
        if l._prev is None:
            temp = self._front
            self._front = r._prev._next
            r._prev._next = temp
            
        elif r._prev is None:
            temp = l._prev._next
            l._prev._next = self._front
            self._front = temp
        
        else:
            temp = l._prev._next
            l._prev._next = r._prev._next
            r._prev._next = temp
            
        if l._next is None:
            temp = self._rear
            self._rear = r._next._prev
            r._next._prev = temp
            
        elif r._next is None:
            temp = l._next._prev
            l._next._prev = self._rear
            self._rear = temp
        
        else:
            temp = l._next._prev
            l._next._prev = r._next._prev
            r._next._prev = temp
            
        temp = l._next
        l._next = r._next
        r._next = temp
      
        temp = l._prev
        l._prev = r._prev
        r._prev = temp
        
        return
        
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the dequeue
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the dequeue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next