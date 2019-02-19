"""
-------------------------------------------------------
test_sorts_linked.py
Tests various linked sorting functions.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
"""
# Imports
import random
from list_linked import List
from number import Number
from sorts_list_linked import Sorts


# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Create a sorted list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns:
        values - a sorted list of SIZE Number objects (List)
    -------------------------------------------------------
    """
    values = List()
    
    for i in range(SIZE+1):
        values.insert(i,Number(i))
    
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        values - a reversed list of SIZE Number objects (List)
    -------------------------------------------------------
    """    
    values = List()
    
    spot = 0
    for i in range(SIZE-1,-1,-1):
        values.insert(spot,Number(i))
        spot +=1 
    
    return values



def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        lists: TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List)
    -------------------------------------------------------
    """
    lists = List()
    
    for i in range(TESTS):
        l = List()
        for j in range(SIZE):
            num = Number(random.randint(0,XRANGE))
            l.insert(j, num)
            
        lists.insert(i, l)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and print out
    its comparisons for sorted, reversed, and random lists
    of data.
    -------------------------------------------------------
    Preconditions:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Postconditions:
        prints the number of comparisons necessary to sort a
        list: in order, in reverse order, and a list of arrays
        in random order.
    -------------------------------------------------------
    """
    s = create_sorted()
    r = create_reversed()
    rand = create_randoms()
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    func(s)
    
    s_comp = Number.comparisons
    s_swap = Sorts.swaps
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    func(r)
    
    r_comp = Number.comparisons
    r_swap = Sorts.swaps
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    for i in range(TESTS):
        func(rand[i])
    
    rand_comp = int(Number.comparisons/len(rand))
    rand_swap = int(Sorts.swaps/len(rand))
    
    print("{}\t {}\t {}\t {}\t\t{}\t{}\t{}".format(title,s_comp,r_comp,rand_comp, s_swap,r_swap,rand_swap))
    

    return
