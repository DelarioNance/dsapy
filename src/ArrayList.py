"""
A Python program containing the class definition for my implementation 
of the ArrayList data structure using test-driven development (TDD).

Author: Delario Nance, Jr.
Date: January 24, 2023 - February 19, 2023
"""

# Standard library imports
from __future__ import annotations # for using ArrayList type hint in ArrayList methods
from math import ceil # for rounding up initial ArrayList capacities
import numpy as np
from numpy.typing import NDArray # for NumPy type hints
from typing import Union # for Union type hint

# Global variables
DEFAULT_CAPACITY_BASE = 16 # Chose 16 since 16 is a power of two close to Java's default of 10
VALUE_FOR_INDEX_PAST_CAPACITY = -1
RESIZE_FACTOR = 2 # Not 1.5 to avoid decimal size of NumPy array
INITIAL_VALUE_IN_MERGED_ARR = 0 # Used in _merge method
NP_NDARRAY_DTYPE = np.ndarray

class ArrayList:    
    def __init__(self, values: list[int]) -> None:
        """Constructs an ArrayList object from a 
        user-specified Python list of integers.

        Args:
            values (list[int]): The user-specified Python 
                                list of integers
        """
        if len(values) == 0:
            self._capacity = DEFAULT_CAPACITY_BASE
        else:
            self._capacity = self._round_to_multiple(len(values), DEFAULT_CAPACITY_BASE)
            
        lengthened_values = self._lengthen(values, self._capacity)
        if type(values) == list:
            self._values = np.array(lengthened_values, dtype = int)
        elif type(values) == NP_NDARRAY_DTYPE:
            self._values = lengthened_values
            
        self._next = len(values)
        
    def __len__(self) -> int:
        """Returns the size of this ArrayList.

        Returns:
            int: The size of this ArrayList
        """
        return self._next
    
    def __str__(self) -> NDArray[np.int_]:
        """Returns the string representation of this ArrayList.
        """
        return str(self._values[:self._next])
    
    def __getitem__(self, index: int) -> int:
        """Returns the value at a user-specified index in 
        this ArrayList.

        Args:
            index (int): The user-specified index

        Returns:
            int: The value at the given index
        """
        if index < 0:
            corresponding_positive_index = self._next + index
            return self._values[corresponding_positive_index] 
        return self._values[index]
    
    def __setitem__(self, index: int, value: int) -> None:
        """Sets the value at a user-specified index in this
        ArrayList to a user-specified value

        Args:
            index (int): The user-specified index
            value (int): The user-specified value
        """
        self._values[index] = value
        
    def __eq__(self, lst_to_compare: Union[list[int], ArrayList]) -> bool:
        """Returns true iff this ArrayList contains exactly
        the values in a second user-specified ArrayList to
        compare.

        Args:
            lst_to_compare (ArrayList): The second user-specified 
                                        ArrayList

        Returns:
            bool: True iff this ArrayList and the user-specified
                  ArrayLisy contain the same values
        """
        values_in_this_array = self._values[:len(self)]
        
        if type(lst_to_compare) == ArrayList:    
            values_in_other_array = lst_to_compare._values[:len(lst_to_compare)]
            return np.array_equal(values_in_this_array, values_in_other_array)
        else:
            return np.array_equal(values_in_this_array, lst_to_compare)
    
    def append(self, value: int) -> None:
        """Appends a user-specified value to the end of this
        ArrayList, and increases the capacity of the ArrayList
        if necessary.

        Args:
            value (int): The user-specified value
        """
        if self._next == self._capacity:
            new_size = self._next * RESIZE_FACTOR
            lengthened_arr_of_values = self._lengthen(self._values, new_size)
            self._values = lengthened_arr_of_values
            self._capacity = new_size
            
        self._values[self._next] = value
        self._next += 1        
            
    def remove(self, index: int) -> None:
        """Removes the value at a user-specified index in this
        ArrayList.

        Args:
            index (int): The user-specified index
        """
        removed_value = self._values[index]
        self._shift_values_left(index)
        return removed_value
    
    def is_empty(self) -> bool:
        """Returns true iff this ArrayList is empty.

        Returns:
            bool: True iff this ArrayList is empty
        """
        return self._next == 0
    
    def max(self) -> int:
        """Returns the largest value in this ArrayList.

        Returns:
            int: The maximum value in this ArrayList
        """
        index_of_max = self._index_of_max(0,len(self)-1)
        return self._values[index_of_max]
    
    def min(self) -> int:
        """Returns the smallest value in this ArrayList.

        Returns:
            int: The minimum value in this ArrayList
        """
        index_of_min = self._index_of_min(0,len(self)-1)
        return self._values[index_of_min]
    
    def contains(self, value: int) -> bool:
        """Returns true iff this ArrayList contains a 
        user-specified value

        Args:
            value (int): The user-specified value

        Returns:
            bool: True iff this ArrayList contains the 
        user-specified value
        """
        size = len(self)
        for index in range(size):
            if self._values[index] == value:
                return True
        return False
    
    def copy(self) -> ArrayList:
        """Returns a copy of this ArrayList.

        Returns:
            ArrayList: The copy of this ArrayList
        """
        values = self._values[:self._next]
        pylist_of_values = [x for x in values]
        return ArrayList(pylist_of_values)
    
    def reverse(self) -> None:
        """Reverses this ArrayList in-place.
        
        To get a reversed version of this ArrayList
        instead of reversing this ArrayList in-place,
        please create a copy of this ArrayList and
        then reverse that copy, as shown below:
        
            array_list = ArrayList([1,2,3,4,5])
            
            copy_of_array_list = array_list.copy()
            
            copy_of_array_list.reverse()
            
            reversed_array_list = copy_of_array_list
        """
        size = self._next
        
        for index in range(size//2):
            mirror_index = size-index-1
            self._swap(index,mirror_index)
            
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
                                      in this ArrayList will be
                                      sorted in ascending order. 
                                      Defaults to False.
        """
        if reverse == False:
            for curr_index in range(len(self)):
                index_of_next_min = self._index_of_min(curr_index,len(self)-1)
                self._swap(curr_index,index_of_next_min)
        else:
            for curr_index in range(len(self)):
                index_of_next_max = self._index_of_max(curr_index,len(self)-1)
                self._swap(curr_index,index_of_next_max)
                
    def bubblesort(self, reverse: bool = False) -> None:
        """Sorts the values in this ArrayList using bubblesort. 
        Like the selection_sort, insertion_sort, and 
        quicksort methods, the selection_sort method sorts 
        this ArrayList in-place.
        
        By default, the values are sorted in ascending order.
        However, the values can be sorted in descending order
        by setting the reverse parameter to true. For example,
        calling
            ArrayList([6,3,1,5]).bubblesort(True)
        will change the values in the ArrayList to [6,5,3,1].

        Args:
            reverse (bool, optional): If true, then the values
                                      in this ArrayList will be
                                      sorted in ascending order. 
                                      Defaults to False.
        """
        for end_index in range(len(self)-1,0,-1): # Last iteration is index 1
            if reverse == False:
                self._bubble_max_right(end_index)
            else:
                self._bubble_min_right(end_index)
    
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
                                      in this ArrayList will be
                                      sorted in ascending order. 
                                      Defaults to False.
        """
        for index in range(len(self)):
            if reverse == False:
               self._insert_min_in_left_subarray(index)
            else:
                self._insert_max_in_left_subarray(index)
    
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
                                      in this ArrayList will be
                                      sorted in ascending order. 
                                      Defaults to False.
        """        
        values = self._values
        sorted_values = self._mergesort(values, 0, len(self)-1)
        return ArrayList(sorted_values)
    
    def _mergesort(self, arr: NDArray[np.int_], start, end) -> NDArray[np.int_]:
        """Recursively sorts the values within a user-specified
        range in an user-specified NumPy array with mergesort. 
        Called by mergesort.

        Args:
            arr (NDArray[np.int_]): The user-specified NumPy array
            start (_type_): The first index of range (inclusive)
            end (_type_): The last index of range(inclusive)

        Returns:
            NDArray[np.int_]: The sorted array of the original
                              values
        """
        length = end - start + 1
        if length == 1: # Does not handle len-0 case
            return arr[start:start+1]
        
        mid = start + length//2
        left_half = self._mergesort(arr, start, mid-1)
        right_half = self._mergesort(arr, mid, end)
        
        merged = self._merge(left_half, right_half)
        return merged
    
    def _merge(self, left_arr: NDArray[np.int_], right_arr: NDArray[np.int_]) -> NDArray[np.int_]:
        """Merges two user-specified NumPy arrays which are 
        sorted in ascending order into another array sorted 
        in ascending order consisting of the values from the 
        two original arrays.

        Args:
            left (NDArray[np.int_]): The first user-specified array
            right (NDArray[np.int_]): The second user-specified array

        Returns:
            NDArray[np.int_]: The result from merging the left
                              and right arrays
        """
        merged_length = len(left_arr) + len(right_arr)
        merged = np.array([INITIAL_VALUE_IN_MERGED_ARR]*merged_length, dtype = int)
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
    
    def _lengthen(self, values: Union[list[int],NDArray[np.int_]], new_size: int) -> list[int]:
        """Lengthens a user-specified Python list (possibly 
        inside a user-specified NumPy array by copying each 
        value to its same index in a new Python list of a 
        user-specified size.

        Args:
            values (Union[list[int],NDArray[np.int_]]): The user-specified Python list or NumPy array
            new_size (int): The user-specified size of the newly created longer Python list or NumPy array

        Returns:
            list[int]: The newly created longer array
        """
        
        longer_lst = [VALUE_FOR_INDEX_PAST_CAPACITY] * new_size
        for index, value in enumerate(values):
            longer_lst[index] = value
            
        if type(values) == list:    
            return longer_lst
           
        elif type(values) == NP_NDARRAY_DTYPE:
            return np.array(longer_lst, dtype = int)
            
    
    def _round_to_multiple(self, x: int, base: int) -> int:
        """Rounds a user-specified number up to the closest
        multiple of a user-specified base. Inspiration for the
        newest implementation taken from 
        [datagy](https://datagy.io/python-round-to-multiple/).

        Args:
            x (int): The user-specified number to round
            base (int): The user-specified base

        Returns:
            int: The rounded up number to the nearest multiple
                 of base
        """
        return ceil(x/base) * base
    
    def _shift_values_left(self, bound: int) -> None:
        """Shifts every value at an index to the right of a 
        user-specified index in this ArrayList to the left by
        one index, decrementing the size of this ArrayList.

        Args:
            bound (int): The user-specified index
        """
        size = self._next
        for index in range(bound,size-1):
            self._values[index] = self._values[index+1]
        self._values[size-1] = VALUE_FOR_INDEX_PAST_CAPACITY
        
        self._next -= 1
    
    def _is_full(self) -> bool:
        """Returns true iff the size of this ArrayList equals
        its capacity.

        Returns:
            bool: True iff the size of this ArrayList equals
        its capacity
        """
        return len(self) == self._capacity
    
    def _swap(self, index_a: int, index_b: int) -> None:
        """Swaps the values at two user-specified positions
        in this ArrayList.

        Args:
            index_a (int): The first user-specified position
            index_b (int): The second user-specified position
        """
        self._values[index_a],self._values[index_b] = self._values[index_b],self._values[index_a]
        
    def _index_of_max(self, start: int, end: int) -> int:
        """Returns the largest value in a user-specified 
        range in this ArrayList. This "private" method is
        called in the max method.

        Args:
            start (int): The first value in the user-specified
                         range, inclusive
            end (int): The last value in the user-specified
                       range, inclusive

        Returns:
            int: The maximum value in this ArrayList
        """
        index_of_min = start
        
        for curr_index in range(start+1,end+1):
            if self._values[curr_index] > self._values[index_of_min]:
                index_of_min = curr_index
        return index_of_min
    
    def _index_of_min(self, start: int, end: int) -> int:
        """Returns the smallest value in a user-specified 
        range in this ArrayList. This "private" method is
        called in the min and selection_sort methods.

        Args:
            start (int): The first value in the user-specified
                         range, inclusive
            end (int): The last value in the user-specified
                       range, inclusive

        Returns:
            int: The minimum value in this ArrayList
        """
        index_of_min = start
        
        for curr_index in range(start+1,end+1):
            if self._values[curr_index] < self._values[index_of_min]:
                index_of_min = curr_index
        return index_of_min
        
    def _bubble_max_right(self, end_index: int) -> None:
        """Moves the maximum value before a user-specified 
        index in this ArrayList to the given index by 
        repeatedly swapping the position of values at adjacent
        indices if the value in the left index is larger than
        the value in the right index. Called by bubblesort.

        Args:
            end_index (int): The user-specified index to put
                             the maximum value before it in
        """
        for left_index in range(end_index):
            right_index = left_index + 1
            if self[left_index] >= self[right_index]:
                self._swap(left_index, right_index)
                
    def _bubble_min_right(self, end_index: int) -> None:
        """Moves the minimum value before a user-specified 
        index in this ArrayList to the given index by 
        repeatedly swapping the position of values at adjacent
        indices if the value in the left index is smaller than
        the value in the right index. Called by bubblesort.

        Args:
            end_index (int): The user-specified index to put
                             the minimum value before it in
        """
        for left_index in range(end_index):
            right_index = left_index + 1
            if self[left_index] <= self[right_index]:
                self._swap(left_index, right_index)
                
    def _insert_min_in_left_subarray(self, start_index: int) -> None:
        """Repeatedly moves the value at a user-specified 
        index in this ArrayList to the left, swapping 
        positions with its left neighbor, until the value is
        larger than all the values to its left. Called by 
        insertion_sort.

        Args:
            index_of_val_to_move (int): The user-specified 
                                        index of the value
                                        to repeatedly move
                                        to the left
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
        smaller than all the values to its left. Called by 
        insertion_sort.

        Args:
            index_of_val_to_move (int): The user-specified 
                                        index of the value
                                        to repeatedly move
                                        to the left
        """
        curr_index, left_index = start_index, start_index - 1
        while left_index >= 0:
            if self[left_index] > self[curr_index]: # Sorted
                break
            else:
                self._swap(left_index, curr_index)
                curr_index -= 1
                left_index -= 1