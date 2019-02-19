"""
-------------------------------------------------------
queue_circular.py
Array version of the CircularQueue ADT.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
"""


class CircularQueue:

    def __init__(self, max_size):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: cq = CircularQueue(max_size)
        -------------------------------------------------------
        Preconditions:
            max_size - maximum size of the queue (int > 0)
        Postconditions:
            Initializes an empty queue.
        -------------------------------------------------------
        """
        assert max_size > 0, "CircularQueue size must be > 0"

        self._max_size = max_size
        self._values = [None] * self._max_size
        self._front = 0
        self._rear = 0
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = cq.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        result = False
        if self._count == 0:
            result = True
        
        return result
            

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = cq.is_full()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        result = False
        if self._count == self._max_size:
            result = True
            
        return result
            

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(cq)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: cq.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the queue.
        -------------------------------------------------------
        """
        assert self._count < self._max_size, "queue is full"
        self._values[self._rear] = value
        self._rear = (self._rear + 1) % self._max_size
        self._count += 1
            
        return 

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = cq.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of the queue - the value is
            removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty queue"
        value = self._values[self._front]
        self._values[self._front] = None
        self._front = (self._front +1) % self._max_size
        return value
        

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = cq.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of the queue -
            the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"
        value = self._values[self._front]
        return value
        