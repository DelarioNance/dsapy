"""
A Python program containing the class definition for my implementation 
of the ArrayList data structure using test-driven development (TDD).

Author: Delario Nance, Jr.
Date: January 24, 2023 - February 10, 2023
"""

# Standard library imports
from __future__ import annotations # for using ArrayList type hint in ArrayList methods
from math import ceil # for rounding up initial ArrayList capacities
import numpy as np
from numpy.typing import NDArray # for NumPy type hints
from typing import Union # for Union type hint

DEFAULT_CAPACITY_BASE = 16 # Chose 16 since 16 is a power of two close to Java's default of 10
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
        
    def __eq__(self, lst_to_compare: ArrayList) -> bool:
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
        return self._values == lst_to_compare._values
        
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
        self._next -= 1
    
    def is_empty(self) -> bool:
        """Returns true iff this ArrayList is empty.

        Returns:
            bool: True iff this ArrayList is empty
        """
        return self._next == 0
    
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
        longer_array = [-1] * new_size
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
    