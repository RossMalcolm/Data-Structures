"""
-------------------------------------------------------
utilities.py
Utilities
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2018-01-15"
-------------------------------------------------------
"""
from stack_array import Stack
from queue_array import Queue
from list_linked import List
from food import Food
from priority_queue_array import PriorityQueue


def array_to_list(l,a):
    """
    -------------------------------------------------------
    Pushes contents of a onto l
    Use: array_to_list(l, a)
    -------------------------------------------------------
    Preconditions:
        l - a List object (List)
        a - a Python list (List)
    Postconditions:
        The contents of a are moved into s, a is empty.
    -------------------------------------------------------
    """
    while len(a) != 0:
        l.append(a.pop())
    return l
    

def array_to_stack(s, a):
    """
    -------------------------------------------------------
    Pushes contents of a onto s.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        The contents of a are moved into s, a is empty.
    -------------------------------------------------------
    """
    for i in range(len(a)):
        s.push(a.pop(0))
    
    
def stack_to_array(s, a):
    """
    -------------------------------------------------------
    Pops contents of s into a.
    Use: stack_to_array(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        Contents of s are moved into a, s is empty.
    -------------------------------------------------------
    """
    while len(s) != 0:
        a.append(s.pop())
    
def stack_test(a):
    """
    -------------------------------------------------------
    Tests 
    Use: stack_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Stack are tested for both empty and 
        non-empty stacks using the data in a:
        empty, push, pop, peek
    -------------------------------------------------------
    """
    s = Stack()
    
    array_to_stack(s, a)
    
    if s.is_empty() == True:
        print("Stack is empty")
    else:
        print("Stack is not empty")
        
    for i in s:
        print(i)
    
    print("Test Peek: {}".format(s.peek()))
    print("Test pop: {}".format(s.pop()))
    print("Test peek again: {}".format(s.peek()))
    
    

    # tests for the stack methods go here
    # print the results of the method calls and verify by hand

    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        empty, insert, remove, peek
    -------------------------------------------------------
    """
    q = Queue()
    for i in a:
        q.insert(i)

    print("Is the queue empty: {}".format(q.is_empty()))
    print("Removed: {}".format(q.remove()))
    print("Peek {}".format(q.peek()))
    
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of PriorityQueue are tested for both empty and 
        non-empty priority queues using the data in a:
        empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = PriorityQueue()
    for i in a:
        pq.insert(i)
        
    print("Is the queue empty: {}".format(pq.is_empty()))
    print("Removed: {}".format(pq.remove()))
    print("Peek {}".format(pq.peek()))
    
    return

def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    Use: list_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of List are tested for both empty and 
        non-empty lists using the data in a:
        empty, insert, remove, append, index, __contains__,
        find, max, min, __getitem__, __setitem__
    -------------------------------------------------------
    """
    l = List()
    array_to_list(l, a)
    print("Is the list empty: {}".format(l.is_empty()))
    l.insert(0, Food("Junior Chickens",8, None, None))
    print("Inserted in spot 0: {}".format(l[0]))
    print("Removed: {}".format(l.remove(Food("Junior Chickens",8, None, None))))
    l.append(Food("Hot Dogs", 8, None, None))
    print("appended: {}".format(l[-1]))
    print("index of hot dogs is: {}".format(l.index(Food("Hot Dogs", 8, None, None))))
    b = Food("Pavlova", 10, True, 272) in l
    print("Does the list contain Pavlova: {}".format(b))        
    print("Max: {}".format(l.max()))
    print("Min: {}".format(l.min()))
    print("The item at spot 0 is: {}".format(l[0]))     
    l[0] =  Food("Eggplant", 8 , True, 100)    
    print("change the item at spot 0: {}".format(l[0]))                 
    
    
    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    return




        
