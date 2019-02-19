
"""
-------------------------------------------------------
stack_array.py
Array version of the Stack ADT.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-19"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a list.
        Use: s = Stack()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty stack.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns True if the stack is empty, False otherwise.
        -------------------------------------------------------
        """
        empty = False
        
        if len(self._values) == 0:
            empty = True
        return empty


    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto stack.
        Use: s.push(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the top of the stack.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack.
        Use: value = s.pop()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the top of the stack - the value is
                removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"
        value = self._values.pop()
        

        return value
        
    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the top of the stack.
        Use: value = s.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the top of the stack -
                the value is not removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"
        value = deepcopy(self._values[(len(self._values) -1)])
        
        return value
 
    def combine(self, s2):
        """
        -------------------------------------------------------
        Combines a second stack with the current stack.
        (iterative algorithm)
        Use: s3 = s1.combine(s2)
        -------------------------------------------------------
        Preconditions:
            s2 - an array-based stack (Stack)
        Postconditions:
            Returns:
            s3 - the contents of the current stack and s2
                are interlaced into s3 - current stack and s2
                are empty (Stack)
        -------------------------------------------------------
        """
        s3 = Stack()
        while len(self._values) != 0 or len(s2._values):
            if len(self._values) != 0:
                s3._values.append(deepcopy(self._values.pop()))
            if len(s2._values) != 0:
                s3._values.append(deepcopy(s2._values.pop()))

        return s3

    def split(self):
        """
        -------------------------------------------------------
        Splits the current stack into separate stacks. Current stack is empty
        when operation is done.
        Use: s2, s3 = s1.split()
        -------------------------------------------------------
        Postconditions:
            returns
            s2 - contains alternating values from current stack (Stack)
            s3 - contains other alternating values from current stack (Stack)
        -------------------------------------------------------
        """
        s2 = Stack()
        s3 = Stack()
        while self.is_empty() == False:
            if self.is_empty() == False:
                s2._values.append(self._values.pop())
            if self.is_empty() == False:
                s3._values.append(self._values.pop())

        return s2, s3

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Postconditions:
            returns
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value