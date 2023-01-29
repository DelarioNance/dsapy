"""
A Python program containing the class definition for my implementation 
of the ArrayList data structure using test-driven development (TDD).

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 27, 2023
"""

# Standard library imports
from dataclasses import dataclass
import numpy as np


@dataclass
class ArrayList:
    """_summary_
    """
    def __init__(self, values: list[float]) -> None:
        """Constructs an ArrayList object from a user-specified list of numbers.

        Args:
            values (list[float]): The user-specified list of numbers
        """
        self._size = len(values)
        
    def __len__(self) -> int:
        """Returns the size of this ArrayList.

        Returns:
            int: The size of this ArrayList
        """
        return self._size