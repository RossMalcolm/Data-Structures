"""
-------------------------------------------------------
test_sorts_array.py
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
"""
# Imports
import random
from number import Number
from sorts_array import Sorts

from copy import deepcopy

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
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)

#   ('BST Sort', Sorts.bst_sort),
def create_sorted():
    """
    -------------------------------------------------------
    Create a sorted list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        values - a sorted list of SIZE Number objects.
    -------------------------------------------------------
    """
    values = []
    for i in range(SIZE):
        values.append(Number(i))

    return deepcopy(values)


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        values - a reversed list of SIZE Number objects.
    -------------------------------------------------------
    """
    values = []
    
    for i in range(SIZE-1,-1,-1):
        
        values.append(Number(i))
        
    return deepcopy(values)


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    -------------------------------------------------------
    Postconditions:
        returns
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE.
    -------------------------------------------------------
    """
    arrays = []
    
    for i in range(TESTS):
        l = []
            
        for j in range(SIZE):
            num = Number(random.randint(0,XRANGE))
            l.append(num)
            
        arrays.append(l)

    return deepcopy(arrays)


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and print out
    its comparisons for sorted, reversed, and random arrays
    of data.
    -------------------------------------------------------
    Preconditions:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Postconditions:
        prints the number of comparisons necessary to sort an
        array: in order, in reverse order, and a list of arrays
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
    
    rand_comp = Number.comparisons // TESTS
    rand_swap = Sorts.swaps // TESTS
    
    print("{}\t {}\t {}\t {}\t\t{:.0f}\t{:.0f}\t{:.0f}".format(title,s_comp,r_comp,rand_comp, s_swap,r_swap,rand_swap))
    

    return