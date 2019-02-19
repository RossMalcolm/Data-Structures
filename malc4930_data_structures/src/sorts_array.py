"""
-------------------------------------------------------
sorts_array.py
Array versions of various sorts.
-------------------------------------------------------
Author:  Ross Malcolm
ID:      170514930
Email:   malc4930@mylaurier.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
"""

from bst_linked import BST


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of array-based sort operations.
    Uses class attribute 'swaps' to determine how many times 
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def selection_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Selection Sort algorithm.
        Use: Sorts.selection_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - a Python list of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        n = len(a)
        i = 0

        while i < n:
            # Walk through entire array
            m = i
            j = i + 1

            while j < n:
                # Find smallest value in unsorted part of array

                if a[m] > a[j]:
                    # Track smallest value so far
                    m = j
                j += 1

            if m != i:
                # swap elements only if necessary
                Sorts._swap(a, m, i)
            i = i + 1
        return

    @staticmethod
    def insertion_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Insertion Sort algorithm.
        Use: Sorts.insertion_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        n = len(a)
        i = 1

        while i < n:
            # Walk through entire array
            # Move each key bigger than save in a[1:n-1] one space to right.
            save = a[i]
            # Count as a swap
            Sorts.swaps += 1
            j = i - 1

            while j >= 0 and a[j] > save:
                Sorts._shift(a, j + 1, j)
                j -= 1
            # Move save into hole opened up by moving previous keys to right.
            a[j + 1] = save
            i += 1
        return

    @staticmethod
    def bubble_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Bubble Sort algorithm.
        Use: Sorts.bubble_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        done = False
        last = len(a) - 1

        while not done:
            # assume done is true
            done = True
            last_swapped = 0
            i = 0

            while i < last:
                if a[i] > a[i + 1]:
                    # Save the list index swapped.
                    last_swapped = i
                    # The pair (a[i], a[i+1]) is out of order.
                    # Exchange a[i] and a[i + 1] to put them in sorted order.
                    Sorts._swap(a, i, i + 1)
                    # If you swapped you need another pass.
                    done = False
                i += 1
            last = last_swapped
            # Decreases 'last' because everything after last_swapped is already
            # in order. done == False iff no pair of keys swapped on last pass.
        return

    @staticmethod
    def bst_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Tree Sort algorithm.
        Use: Sorts.bst_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        bst = BST()

        for v in a:
            bst.insert(v)

        a[:] = bst.traverse()
        return

    @staticmethod
    def shell_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Shell Sort algorithm.
        Use: Sorts.shell_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        n = len(a)
        increment = n // 3

        while increment > 0:
            i = increment

            while i < n:
                j = i
                temp = a[i]

                while j >= increment and a[j - increment] > temp:
                    Sorts._shift(a, j, j - increment)
                    j = j - increment
                a[j] = temp
                i += 1

            increment = increment // 3
        return

    @staticmethod
    def merge_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Merge Sort algorithm.
        Use: Sorts.merge_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        Sorts._merge_sort_aux(a, 0, len(a) - 1)
        return

    @staticmethod
    def _merge_sort_aux(a, first, last):
        """
        -------------------------------------------------------
        Divides an array into halves, sorts each half, then
        merges the halves back together.
        Use: Sorts._merge_sort_aux(a, first, last)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
            first - beginning of subarray of a (int)
            last - end of subarray of a (int)
        Postconditions:
            Contents of a from first to last are sorted.
        -------------------------------------------------------
        """

        if first < last:
            middle = (last - first) // 2 + first
            Sorts._merge_sort_aux(a, first, middle)
            Sorts._merge_sort_aux(a, middle + 1, last)
            Sorts._merge(a, first, middle, last)
        return

    @staticmethod
    def _merge(a, first, middle, last):
        """
        -------------------------------------------------------
        Merges two parts of an array together.
        Use: Sorts._merge(a, first, middle, last)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
            first - beginning of subarray of a (int)
            middle - middle of subarray of a (int)
            last - end of subarray of a (int)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        temp = []
        i = first
        j = middle + 1

        while i <= middle and j <= last:

            if a[i] <= a[j]:
                # put leftmost element of left array into temp array
                temp.append(a[i])
                i += 1
            else:
                # put leftmost element of right array into temp array
                temp.append(a[j])
                j += 1

        # copy any remaining elements from the left half
        while i <= middle:
            temp.append(a[i])
            i += 1

        # copy any remaining elements from the right half
        while j <= last:
            temp.append(a[j])
            j += 1

        # copy the temporary array back to the passed array
        i = 0

        while i < len(temp):
            a[first + i] = temp[i]
            i += 1
        return

    @staticmethod
    def quick_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Quick Sort algorithm.
        Use: Sorts.quick_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        Sorts._quick_sort_aux(a, 0, len(a) - 1)
        return

    @staticmethod
    def _quick_sort_aux(a, first, last):
        """
        -------------------------------------------------------
        Divides an array into halves, sorts each half, then
        concatenates the halves back together.
        Use: Sorts._quick_sort_aux(a, first, last)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
            first - beginning of subarray of a (int)
            last - end of subarray of a (int)
        Postconditions:
            Contents of a from first to last are sorted.
        -------------------------------------------------------
        """
        # to sort the subarray a[p:q] of array a into ascending order
        if first < last:
            # partitions a[first:last] into a[first:pivot] and a[pivot+1:last]
            i = Sorts._partition(a, first, last)
            Sorts._quick_sort_aux(a, first, i - 1)
            Sorts._quick_sort_aux(a, i + 1, last)
        return

    @staticmethod
    def _partition(a, first, last):
        """
        -------------------------------------------------------
        Divides an array into two parts.
        Use: Sorts._partition(a, first, last)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
            first - beginning of subarray of a (int)
            last - last of subarray of a (int)
        Postconditions:
            Contents of a from first to last are sorted.
        -------------------------------------------------------
        """
        pivot_index = first
        low = first
        high = last - 1  # After we remove pivot it will be one smaller
        # print("{} - {} - {}".format(a[first:pivot_index], a[pivot_index],
        #                        a[pivot_index + 1:last]))
        pivot_value = a[pivot_index]
        a[pivot_index] = a[last]

        while low <= high:
            # print("{} - {} - {}".format(a[first:pivot_index],
            #        a[pivot_index], a[pivot_index + 1:last]))
            while low <= high and a[low] < pivot_value:
                low = low + 1
            while low <= high and a[high] >= pivot_value:
                high = high - 1
            if low <= high:
                Sorts._swap(a, low, high)
        Sorts._shift(a, last, low)
        # a[last] = a[low]
        a[low] = pivot_value
        # print("{} - {} - {}".format(a[first:pivot_index], a[pivot_index],
        #                   a[pivot_index + 1:last]))
        # Return the new pivot position.
        return low

    @staticmethod
    def heap_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Heap Sort algorithm.
        Use: Sorts.heap_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        first = 0
        last = len(a) - 1
        Sorts._build_heap(a, first, last)
        i = last

        while i > first:
            Sorts._swap(a, i, first)
            Sorts._reheap(a, first, i - 1)
            i -= 1
        return

    @staticmethod
    def _build_heap(a, first, last):
        """
        -------------------------------------------------------
        Creates a heap.
        Use: Sorts._build_heap(a, first, last)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (list)
            first - first element in array to process (int)
            last - last element in array to process (int)
        Postconditions:
            Contents of a from first to last are sorted.
        -------------------------------------------------------
        """
        i = last // 2

        while i >= first:
            Sorts._reheap(a, i, last)
            i -= 1
        return

    @staticmethod
    def _reheap(a, first, last):
        """
        -------------------------------------------------------
        Establishes heap property in a.
        Use: Sorts._reheap(a, first, last)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
            first - first element in array to process (int)
            last - last element in array to process (int)
        Postconditions:
            Contents of a from first to last are heaped.
        -------------------------------------------------------
        """
        done = False

        while 2 * first + 1 <= last and not done:
            k = 2 * first + 1

            if k < last and a[k] < a[k + 1]:
                k += 1

            if a[first] >= a[k]:
                done = True
            else:
                Sorts._swap(a, first, k)
                first = k
        return

    @staticmethod
    def comb_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Comb Sort algorithm.
        Use: Sorts.comb_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        n = len(a)
        gap = n
        done = False

        while gap > 1 or not done:
            done = True
            gap = int(gap / 1.3)

            if gap < 1:
                gap = 1

            i = 0
            j = gap

            while j < n:
                if a[i] > a[j]:
                    Sorts._swap(a, i, j)
                    done = False
                i += 1
                j += 1
        return

    @staticmethod
    def cocktail_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Cocktail Sort algorithm.
        Use: Sorts.cocktail_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        n = len(a)
        first = 0
        last = n - 1

        while first < last:
            # Initialize last_swapped to the beginning of the array.
            # Stops bottom loop from executing if no swaps done by top loop.
            last_swapped = 0
            i = first

            while i < last:
                if a[i] > a[i + 1]:
                    # test whether the two elements are in the correct order
                    Sorts._swap(a, i, i + 1)
                    last_swapped = i
                i += 1
            last = last_swapped

            # Initialize first_swapped to the end of the array.
            # Stops top loop from executing if no swaps done by bottom loop.
            first_swapped = n - 1
            i = last

            while i > first:
                if a[i] < a[i - 1]:
                    # test whether the two elements are in the correct order
                    Sorts._swap(a, i, i - 1)
                    first_swapped = i
                i -= 1
            first = first_swapped
        return

    @staticmethod
    def binary_insert_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Binary Insertion Sort algorithm.
        Use: Sorts.binary_insert_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (list)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        n = len(a)
        i = 1

        while i < n:
            ins = Sorts._bin_srch_i(a, 0, i, a[i])
            # Move key bigger than save in a[1:n-1] one space to the right.
            if ins < i:
                save = a[i]
                j = i - 1

                while j > ins - 1:
                    Sorts._shift(a, j + 1, j)
                    # a[j + 1] = a[j]
                    j -= 1
                a[ins] = save
            i += 1
        return

    @staticmethod
    def _bin_srch_r(a, low, high, value):
        """
        -------------------------------------------------------
        Sorts an array using the Binary Insertion Sort algorithm.
        Use: Sorts._bin_srch_r(a)
        Recursive algorithm.
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (list)
            low - starting point of a to search for value (int)
            high - end point of a to search for value (int)
            value - value to search for position in a (?)
        Postconditions:
            returns
            mid - the insert point for value in a between low and high
        -------------------------------------------------------
        """
        if low == high:
            mid = low
        else:
            mid = low + ((high - low) // 2)

            if value > a[mid]:
                mid = Sorts._bin_srch_r(a, mid + 1, high, value)
            elif value < a[mid]:
                mid = Sorts._bin_srch_r(a, low, mid, value)
        return mid

    @staticmethod
    def _bin_srch_i(a, low, high, value):
        """
        -------------------------------------------------------
        Sorts an array using the Binary Insertion Sort algorithm.
        Use: Sorts._bin_srch_r(a)
        Iterative algorithm.
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (list)
            low - starting point of a to search for value (int)
            high - end point of a to search for value (int)
            value - value to search for position in a (?)
        Postconditions:
            returns
            mid - the insert point for value in a between low and high
        -------------------------------------------------------
        """
        found = False
        mid = (low + high) // 2

        while low < high and not found:
            # Find the middle of the current subarray.
            if value > a[mid]:
                # Search the right subarray.
                low = mid + 1
                mid = (low + high) // 2
            elif value < a[mid]:
                # Search the left subarray.
                high = mid
                mid = (low + high) // 2
            else:
                found = True
        return mid

    # Sort Utilities

    @staticmethod
    def sort_test(a):
        """
        -------------------------------------------------------
        Determines whether an array is is_sorted or not.
        Use: sort_test(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
        Postconditions:
            returns
            is_sorted - True if contents of a are sorted, 
                False otherwise.
        -------------------------------------------------------
        """
        is_sorted = True
        n = len(a)
        i = 0

        while is_sorted and i < n - 1:

            if a[i] <= a[i + 1]:
                i += 1
            else:
                is_sorted = False
        return is_sorted

    @staticmethod
    def _swap(a, i, j):
        """
        -------------------------------------------------------
        Swaps the data contents of two array elements.
        Updates 'swaps'.
        Use: Sorts._swap(a, i, j)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
            i - index of one value (int 0 <= i < len(a))
            j - index of another value (int 0 <= j < len(a))
        Postconditions:
            Values in a[i] and a[j] are swapped.
        -------------------------------------------------------
        """
        Sorts.swaps += 1

        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        return

    @staticmethod
    def _shift(a, i, j):
        """
        -------------------------------------------------------
        Shifts the contents of a[j] to a[i].
        Updates 'swaps' - worth 1/3 of _swap
        Use: Sorts._shift(a, i, j)
        -------------------------------------------------------
        Preconditions:
            a - an array of comparable elements (?)
            i - index of one value (int 0 <= i < len(a))
            j - index of another value (int 0 <= j < len(a))
        Postconditions:
            Value in a[j] is copied to a[i].
        -------------------------------------------------------
        """
        Sorts.swaps += 0.34

        a[i] = a[j]
        return
    
    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort.
        Use: Sorts.radix_sort(a)
        -------------------------------------------------------
        Preconditions:
            a - an array of base 10 integers (list)
        Postconditions:
            Contents of a are sorted.
        -------------------------------------------------------
        """
        buckets = []
        for i in range(10):
            buckets.append([])
            
        if len(a) != 0:
            max_val = max(a)
        else:
            max_val = 0      
        
        k = 0
        while 10**k <= max_val:    
            while len(a) > 0:
                x = (a[0] % 10**(k+1))//10**k
                buckets[x].append(a.pop(0))
            
            n=0
            while n < len(buckets) :
                while len(buckets[n]) > 0:
                    a.append(buckets[n].pop(0))
                
                n+=1
                
            k += 1
        return
            