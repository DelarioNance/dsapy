"""
A Python program containing the class definition for my implementation 
of the ArrayList data structure using test-driven development (TDD).

Author: Delario Nance, Jr.
Date: January 24, 2023 - February 15, 2023
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
        lengthened_pylist_of_values = self._lengthen(values, self._capacity)
        self._values = np.array(lengthened_pylist_of_values, dtype = int)
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
        values_in_this_array = self._values[:self._next]
        
        if type(lst_to_compare) == ArrayList:    
            values_in_other_array = lst_to_compare._values[:lst_to_compare._next]
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
            lengthened_pylist_of_values = self._lengthen(self._values, new_size)
            self._values = np.array(lengthened_pylist_of_values)
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
        max_value = self._values[0]
        
        # Not splicing NumPy array since that uses more space
        size = len(self)
        for index in range(1,size):
            if self._values[index] > max_value:
                max_value = self._values[index]
        return max_value
    
    def min(self) -> int:
        """Returns the smallest value in this ArrayList.

        Returns:
            int: The minimum value in this ArrayList
        """
        min_value = self._values[0]
        
        # Not splicing NumPy array since that uses more space
        size = len(self)
        for index in range(1,size):
            if self._values[index] < min_value:
                min_value = self._values[index]
        return min_value
    
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
        return ArrayList(self._values[:self._next])
    
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
            
    
        1:
        2: [0,1) (2//1 = 1)
        3: [0,1) 0 or 0-1 (3//2 = 1)
        4: 0-1 (4//2 = 2)
        5: 0-1 or 0-1-2 (5//2 = 2)
        6: 0-1-2 (6//2 = 3)
        
        [0,1,2,3,4]
        index = [0,2] [0,3)
        [0,1,2,3,4,5]
        index = [0,2] [0,3)
         
    def _lengthen(self, values: Union[list[int],NDArray[np.int_]], new_size: int) -> list[int]:
        """Lengthens a user-specified Python list (possibly 
        inside a user-specified NumPy array by copying each 
        value to its same index in a new Python list of a 
        user-specified size.

        Args:
            values (Union[list[int],NDArray[np.int_]]): The user-specified Python list or NumPy array
            new_size (int): The user-specified size of the newly created longer array

        Returns:
            list[int]: The newly created longer array
        """
        longer_array = [VALUE_FOR_INDEX_PAST_CAPACITY] * new_size
        for index, value in enumerate(values):
            longer_array[index] = value
        return longer_array
    
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
        one index, decrementing the size of tthis ArrayList.

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
        