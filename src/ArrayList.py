"""
A Python program containing the class definition for my implementation 
of the ArrayList data structure using test-driven development (TDD).

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 28, 2023
"""

# Standard library imports
from dataclasses import dataclass
import numpy as np
from numpy.typing import NDArray


@dataclass
class ArrayList:
    """_summary_
    """
    def __init__(self, values: list[int]) -> None:
        """Constructs an ArrayList object from a 
           user-specified list of numbers.

        Args:
            values (list[int]): The user-specified list of 
                                  numbers
        """
        self._values = np.array(values, dtype = int)
        self._size = len(values)
        
    def __len__(self) -> int:
        """Returns the size of this ArrayList.

        Returns:
            int: The size of this ArrayList
        """
        return self._size
    
    def __str__(self) -> NDArray[np.int_]:
        """Returns the string representation of this ArrayList.
        """
        return str(self._values)
    
    def __getitem__(self, index: int) -> int:
        """Returns the value at a user-specified index in 
           this ArrayList.

        Args:
            index (int): The user-specified index

        Returns:
            int: The value at the given index
        """
        return self._values[index]
    
    def is_empty(self) -> bool:
        """Returns true iff this ArrayList is empty.

        Returns:
            bool: True iff this ArrayList is empty
        """
        return self._size == 0