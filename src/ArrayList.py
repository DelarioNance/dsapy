"""
A Python program containing the class definition for my implementation 
of the ArrayList data structure using test-driven development (TDD).

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 24, 2023
"""

from dataclasses import dataclass
import numpy as np

@dataclass
class ArrayList:
    """_summary_
    """
    values: np.ndarray = np.array([])
