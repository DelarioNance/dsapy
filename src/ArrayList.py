"""
A Python program containing the class definition for my implementation 
of the ArrayList data structure using test-driven development (TDD).

Author: Delario Nance, Jr.
Date: January 24, 2023 - March 17, 2023
"""

# Standard library imports
from __future__ import annotations # for using ArrayList type hint in ArrayList methods
from math import ceil # for rounding up initial ArrayList capacities
import numpy as np
from numpy.typing import NDArray # for NumPy type hints
import random
from typing import Union # for Union type hint

# Global variables
DEFAULT_CAPACITY_BASE = 16 # Because 16 is a power of two close to Java's default of 10
VALUE_FOR_INDEX_PAST_CAPACITY = -1
RESIZE_FACTOR = 2 # Not 1.5 to avoid decimal size of NumPy array
INITIAL_VALUE_IN_MERGED_ARR = 0 # Used in _merge method
NP_NDARRAY_DTYPE = np.ndarray
ARRAYLIST_INPUT_TYPES = Union[list[int],NDArray[np.int_]]

class ArrayList:
    def __init__(self, values: ARRAYLIST_INPUT_TYPES) -> None:
        """Constructs an ArrayList object containing the
        values from a user-specified Python list or NumPy
        array of ints.

        Args:
            values (ARRAYLIST_INPUT_TYPES): The user-specified
            Python list or NumPy array of ints
        """
        if len(values) == 0:
            self._capacity = DEFAULT_CAPACITY_BASE
        else:
            self._capacity = self._round_to_next_multiple(len(values), DEFAULT_CAPACITY_BASE)
            
        lengthened_values = self._lengthen(values, self._capacity)
        if type(values) == list:
            self._values = np.array(lengthened_values, dtype = int)
        elif type(values) == NP_NDARRAY_DTYPE:
            self._values = lengthened_values
            
        self._next = len(values)
        
    def _round_to_next_multiple(self, val: int, base_of_multiple: int) -> int:
        """Finds the multiple of a user-specified base
        that a user-specified number is closest to and returns
        the multiple. Inspiration for the newest implementation
        taken from [datagy](https://datagy.io/python-round-to-multiple/).

        Args:
            x (int): The user-specified number to round
            base_of_multiple (int): The user-specified base
            to return a multiple of

        Returns:
            int: The rounded up number to the nearest multiple
                 of base
        """
        return ceil(val/base_of_multiple) * base_of_multiple
    
    def _lengthen(self, values: ARRAYLIST_INPUT_TYPES, new_size: int) -> ARRAYLIST_INPUT_TYPES:
        """Lengthens a user-specified Python list or NumPy
        array to a new user-specified size by returning a
        Python list or NumPy array containing each value from
        the original list or array at the same indices, but
        with the ArrayList class's default values past the 
        indices of the old values.

        Args:
            values (ARRAYLIST_INPUT_TYPES): The user-specified Python list or NumPy array
            new_size (int): The user-specified size of the newly created longer Python list or NumPy array

        Returns:
            ARRAYLIST_INPUT_TYPES: The newly created longer array
        """
        lengthened_values = [VALUE_FOR_INDEX_PAST_CAPACITY] * new_size
        for index, val in enumerate(values):
            lengthened_values[index] = val
            
        if type(values) == list:    
            return lengthened_values
           
        elif type(values) == NP_NDARRAY_DTYPE:
            return np.array(lengthened_values, dtype = int)
        
    def __len__(self) -> int:
        """Returns the size of this ArrayList.

        Returns:
            int: The size of this ArrayList
        """
        return self._next
    
    def __getitem__(self, index: int) -> int:
        """Returns the value at a user-specified index in 
        this ArrayList.

        Args:
            index (int): The user-specified index

        Returns:
            int: The value at the given index
        """
        if index >= 0:
            return self._values[index]
        else:
            positive_index = self._get_corresponding_positive_index(index)
            return self._values[positive_index]
    
    def __setitem__(self, index: int, val: int) -> None:
        """Sets the value at a user-specified index in this
        ArrayList to a user-specified value.

        Args:
            index (int): The user-specified index
            val (int): The user-specified value
        """
        if index >= 0:
            self._values[index] = val
        else:
            positive_index = self._get_corresponding_positive_index(index)
            self._values[positive_index] = val 
    
    def _get_corresponding_positive_index(self, negative_index: int) -> int:
        """Returns the positive index which corresponding to
        a user-specified negative index in this ArrayList

        Args:
            negative_index (int): The user-specified negative index

        Returns:
            int: The corresponding positive index
        """
        return len(self) + negative_index
    
    def __contains__(self, target: int) -> bool:
        """Returns true iff this ArrayList contains a 
        user-specified value.

        Args:
            target (int): The user-specified value to search for

        Returns:
            bool: True iff this ArrayList contains the
            user-specified value
        """
        for index in range(len(self)):
            if self[index] == target:
                return True
        return False
    
    def __eq__(self, lst_to_compare: Union[list[int], ArrayList]) -> bool:
        """Returns true iff this ArrayList and a 
        user-specified Python list or second ArrayList contain
        the same values at the same indices.

        Args:
            lst_to_compare (Union[list[int], ArrayList]): The 
            user-specified Python list or second ArrayList 
            to compare this ArrayList with

        Returns:
            bool: True iff this ArrayList and the given Python
            list or second ArrayList contain the same values at
            the same indices
        """
        if len(self) != len(lst_to_compare):
            return False
        
        for index in range(len(self)):
            if self[index] != lst_to_compare[index]:
                return False
        return True    
    
    def __str__(self) -> NDArray[np.int_]:
        """Returns the string representation of this ArrayList.
        """
        return str(self._values[:len(self)])
    
    def append(self, value: int) -> None:
        """Appends a user-specified value to the end of this
        ArrayList.

        Args:
            value (int): The user-specified value
        """
        if len(self) == self._capacity:
            new_capacity = len(self) * RESIZE_FACTOR
            lengthened_arr_of_values = self._lengthen(self._values, new_capacity)
            self._values = lengthened_arr_of_values
            self._capacity = new_capacity
            
        self[len(self)] = value
        self._next += 1        
            
    def remove(self, index: int) -> None:
        """Removes the value at a user-specified index in this
        ArrayList.

        Args:
            index (int): The user-specified index
        """
        removed_value = self[index]
        
        if index >= 0:
            self._shift_values_left_to_index(index)
        else:
            positive_index = self._get_corresponding_positive_index(index)
            self._shift_values_left_to_index(positive_index)
            
        return removed_value
    
    def _shift_values_left_to_index(self, bound: int) -> None:
        """Shifts every value at an index to the right of a 
        user-specified index in this ArrayList to the left by
        one index, decrementing the size of this ArrayList.

        Args:
            bound (int): The user-specified index
        """
        for index in range(bound,len(self)-1):
            self[index] = self[index+1]
        self[len(self)-1] = VALUE_FOR_INDEX_PAST_CAPACITY
        
        self._next -= 1
    
    def max(self) -> int:
        """Returns the largest value in this ArrayList.

        Returns:
            int: The maximum value in this ArrayList
        """
        index_of_max = self._get_index_of_max(0,len(self)-1)
        return self[index_of_max]
    
    def _get_index_of_max(self, start: int, end: int) -> int:
        """Returns the index of the largest value in a
        user-specified range in this ArrayList.

        Args:
            start (int): The first value in the user-specified
            range (inclusive)
            end (int): The last value in the user-specified
            range (inclusive)

        Returns:
            int: The index of the maximum value in this 
            ArrayList
        """
        index_of_max = start
        
        for index in range(start+1,end+1):
            if self[index] > self[index_of_max]:
                index_of_max = index
        return index_of_max
    
    def min(self) -> int:
        """Returns the smallest value in this ArrayList.

        Returns:
            int: The minimum value in this ArrayList
        """
        index_of_min = self._get_index_of_min(0,len(self)-1)
        return self[index_of_min]
    
    def _get_index_of_min(self, start: int, end: int) -> int:
        """Returns the index of the smallest value in a
        user-specified range in this ArrayList.

        Args:
            start (int): The first value in the user-specified 
            range (inclusive)
            end (int): The last value in the user-specified
            range (inclusive)

        Returns:
            int: The index of the minimum value in this 
            ArrayList
        """
        index_of_min = start
        
        for index in range(start+1,end+1):
            if self[index] < self[index_of_min]:
                index_of_min = index
        return index_of_min
    
    def copy(self) -> ArrayList:
        """Returns a copy of this ArrayList.

        Returns:
            ArrayList: The copy of this ArrayList
        """
        pylist_of_values = [self[index] for index in range(len(self))]
        return ArrayList(pylist_of_values)
    
    def reverse(self) -> None:
        """Reverses this ArrayList in-place.
        
        To get a reversed copy of this ArrayList
        instead of reversing this ArrayList in-place,
        please create a copy of this ArrayList and
        then reverse that copy, as shown below:
        
            array_list = ArrayList([1,2,3,4,5])
            
            copy_of_array_list = array_list.copy()
            
            copy_of_array_list.reverse()
            
            reversed_array_list = copy_of_array_list
        """
        size = len(self)
        
        for index in range(size//2):
            mirror_index = size-index-1
            self._swap(index, mirror_index)
            
    def _swap(self, index_a: int, index_b: int) -> None:
        """Swaps the values at two user-specified indices
        in this ArrayList.

        Args:
            index_a (int): The first user-specified index
            index_b (int): The second user-specified index
        """
        self[index_a], self[index_b] = self[index_b], self[index_a]
     
    def selection_sort(self, reverse: bool = False) -> None:
        """Sorts the values in this ArrayList using selection
        sort. Like the bubblesort, insertion_sort, and 
        quicksort methods, the selection_sort method sorts 
        this ArrayList in-place.
        
        By default, the values are sorted in ascending order.
        However, the values can be sorted in descending order
        by setting the reverse parameter to true. For example,
        calling
            ArrayList([6,3,1,5]).selection_sort(True)
        will change the values in the ArrayList to [6,5,3,1].

        Args:
            reverse (bool, optional): If true, then the values
            in this ArrayList will be sorted in ascending 
            order. Defaults to False.
        """
        if reverse == False:
            for curr_index in range(len(self)):
                index_of_next_min = self._get_index_of_min(curr_index, len(self)-1)
                self._swap(curr_index, index_of_next_min)
        else:
            for curr_index in range(len(self)):
                index_of_next_max = self._get_index_of_max(curr_index, len(self)-1)
                self._swap(curr_index, index_of_next_max)
        
    def bubblesort(self, reverse: bool = False) -> None:
        """Sorts the values in this ArrayList using bubblesort. 
        Like the selection_sort, insertion_sort, and 
        quicksort methods, the bubblesort method sorts 
        this ArrayList in-place.
        
        By default, the values are sorted in ascending order.
        However, the values can be sorted in descending order
        by setting the reverse parameter to true. For example,
        calling
            ArrayList([6,3,1,5]).bubblesort(True)
        will change the values in the ArrayList to [6,5,3,1].

        Args:
            reverse (bool, optional): If true, then the values
            in this ArrayList will be sorted in ascending 
            order. Defaults to False.
        """
        for end_index in range(len(self)-1,0,-1): # Last iteration is index 1
            if reverse == False:
                self._bubble_max_right(end_index)
            else:
                self._bubble_min_right(end_index)
    
    def _bubble_max_right(self, end_index: int) -> None:
        """Moves the maximum value before a user-specified 
        index in this ArrayList to the given index by 
        repeatedly swapping the positions of values at 
        adjacent indices if the value in the left index is 
        larger than the value in the right index.

        Args:
            end_index (int): The user-specified index to put
            the maximum value before it in
        """
        for left_index in range(end_index):
            right_index = left_index + 1
            if self[left_index] > self[right_index]:
                self._swap(left_index, right_index)
                
    def _bubble_min_right(self, end_index: int) -> None:
        """Moves the minimum value before a user-specified 
        index in this ArrayList to the given index by 
        repeatedly swapping the positions of values at 
        adjacent indices if the value in the left index is 
        smaller than the value in the right index.

        Args:
            end_index (int): The user-specified index to put 
            the minimum value before it in
        """
        for left_index in range(end_index):
            right_index = left_index + 1
            if self[left_index] < self[right_index]:
                self._swap(left_index, right_index)
                
    def insertion_sort(self, reverse: bool = False) -> None:
        """Sorts the values in this ArrayList using insertion 
        sort. Like the selection_sort, bubblesort, and 
        quicksort methods, the insertion_sort method sorts 
        this ArrayList in-place.
        
        By default, the values are sorted in ascending order.
        However, the values can be sorted in descending order
        by setting the reverse parameter to true. For example,
        calling
            ArrayList([6,3,1,5]).insertion_sort(True)
        will change the values in the ArrayList to [6,5,3,1].

        Args:
            reverse (bool, optional): If true, then the values
            in this ArrayList will be sorted in ascending 
            order. Defaults to False.
        """
        for index in range(len(self)):
            if reverse == False:
               self._insert_min_in_left_subarray(index)
            else:
                self._insert_max_in_left_subarray(index)
                
    def _insert_min_in_left_subarray(self, start_index: int) -> None:
        """Repeatedly moves the value at a user-specified 
        index in this ArrayList to the left, swapping 
        positions with its left neighbor, until the value is
        larger than all the values to its left.

        Args:
            index_of_val_to_move (int): The user-specified 
            index of the value to repeatedly move to the left
        """
        curr_index, left_index = start_index, start_index - 1
        while left_index >= 0:
            if self[left_index] < self[curr_index]: # Sorted
                break
            else:
                self._swap(left_index, curr_index)
                curr_index -= 1
                left_index -= 1
                
    def _insert_max_in_left_subarray(self, start_index: int) -> None:
        """Repeatedly moves the value at a user-specified 
        index in this ArrayList to the left, swapping 
        positions with its left neighbor, until the value is
        smaller than all the values to its left.

        Args:
            index_of_val_to_move (int): The user-specified 
            index of the value to repeatedly move to the left
        """
        curr_index, left_index = start_index, start_index - 1
        while left_index >= 0:
            if self[left_index] > self[curr_index]: # Sorted
                break
            else:
                self._swap(left_index, curr_index)
                curr_index -= 1
                left_index -= 1
    
    def mergesort(self, reverse: bool = False) -> None:
        """Sorts the values in this ArrayList using mergesort. 
        Unlike the selection_sort, bubblesort, and quicksort 
        methods, the mergesort method sorts this ArrayList 
        out-of-place.
        
        By default, the values are sorted in ascending order.
        However, the values can be sorted in descending order
        by setting the reverse parameter to true. For example,
        calling
            ArrayList([6,3,1,5]).merge(True)
        will change the values in the ArrayList to [6,5,3,1].

        Args:
            reverse (bool, optional): If true, then the values
            in this ArrayList will be sorted in ascending 
            order. Defaults to False.
        """
        sorted_values = self._mergesort(0, len(self)-1)
        sorted_ArrayList = ArrayList(sorted_values)
        
        if reverse == True:
            sorted_ArrayList.reverse()
        return sorted_ArrayList
    
    def _mergesort(self, start, end) -> NDArray[np.int_]:
        """Recursively sorts the values within a user-specified
        range in this ArrayList's NumPy array with mergesort.

        Args:
            start (_type_): The first index of range (inclusive)
            end (_type_): The last index of range(inclusive)

        Returns:
            NDArray[np.int_]: The sorted array of the original
            values
        """
        length = end - start + 1
        if length == 0:
            return []
        if length == 1: # Does not handle len-0 case
            return [self[start]]
        
        mid = start + length//2
        left_half = self._mergesort(start, mid-1)
        right_half = self._mergesort(mid, end)
        
        merged = self._merge(left_half, right_half)
        return merged
    
    def _merge(self, left_arr: list[int], right_arr: list[int]) -> list[int]:
        """Merges two user-specified Python lists which are 
        sorted in ascending order into another array sorted 
        in ascending order consisting of the values from the 
        two original arrays.

        Args:
            left (list[int_]): The first user-specified Python
            list
            right (list[int_]): The second user-specified Python
            list

        Returns:
            list[int_]: The result from merging the left
            and right Python lists
        """
        merged_length = len(left_arr) + len(right_arr)
        merged = [INITIAL_VALUE_IN_MERGED_ARR] * merged_length
        left_ptr, right_ptr, merged_ptr = 0, 0, 0
        
        while left_ptr < len(left_arr) or right_ptr < len(right_arr):
            if left_ptr == len(left_arr):
                merged[merged_ptr] = right_arr[right_ptr]
                right_ptr += 1
                
            elif right_ptr == len(right_arr):
                merged[merged_ptr] = left_arr[left_ptr]
                left_ptr += 1
                
            elif left_arr[left_ptr] < right_arr[right_ptr]:
                merged[merged_ptr] = left_arr[left_ptr]
                left_ptr += 1
            
            else:
                merged[merged_ptr] = right_arr[right_ptr]
                right_ptr += 1
                
            merged_ptr += 1
            
        return merged
    
    def quicksort(self, reverse: bool = False) -> None:
        """Sorts the values in this ArrayList using quicksort.
        Like the selection_sort, bubblesort, and
        insertion_sort methods, the quicksort method sorts 
        this ArrayList in-place.
        
        By default, the values are sorted in ascending order.
        However, the values can be sorted in descending order
        by setting the reverse parameter to true. For example,
        calling
            ArrayList([6,3,1,5]).quicksort(True)
        will change the values in the ArrayList to [6,5,3,1].
        
        Args:
            reverse (bool, optional): If true, then the values
            in this ArrayList will be sorted in ascending 
            order. Defaults to False.
        """
        self._quicksort(0, len(self)-1)
        
        if reverse:
            self.reverse()
        
    def _quicksort(self, start: int, end: int) -> None:
        """Sorts the values in a user-specified range in this 
        ArrayList by using a version of quicksort in which the
        pivot value is always the leftmost value in the 
        given range. Recursively puts each value of this 
        ArrayList at its correct position in the final, sorted
        version of this ArrayList.

        Args:
            start (int): The first index in the user-specified
            range (inclusive)
            end (int): The last index in the user-specified
            range (inclusive)
        """
        if start >= end:
            return
        pivot_index = self._partition(start, end)
        self._quicksort(start, pivot_index-1)
        self._quicksort(pivot_index+1, end)
        
    def _partition(self, start: int, end: int) -> int:
        """Selects the leftmost value (known as the "pivot") in 
        a user-specified range in this ArrayList and puts that 
        value at its correct position in the final, sorted 
        version of this ArrayList.

        Args:
            start (int): The first index in the user-specified
            range (inclusive)
            end (int): The last index in the user-specified
            range (inclusive)

        Returns:
            int: The pivot value's index in the final, sorted 
            version of this ArrayList.
        """
        # Initialize start index of pivot
        starting_pivot_index = start
        pivot_val = self[starting_pivot_index]
        
        # Put pivot in correct place
        left = start + 1
        right = end
        
        while True:
            # Move left ptr to first mismatched position
            while left < len(self) and self[left] <= pivot_val:
                left += 1
            
            # Move right ptr to first mismatched position
            while 0 < right and pivot_val < self[right]:
                right -= 1
            
            # Swap left and right values
            if left < right:
                self._swap(left, right)
            else:
                self._swap(starting_pivot_index, right)
                break
                    
        # Return final index of pivot
        ending_pivot_index = right
        return ending_pivot_index