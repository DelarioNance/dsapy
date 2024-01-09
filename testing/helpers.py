"""
A Python program containing the definitions of helper 
functions used in the unit, integration, and end-to-end test
scripts for the ArrayList class.

Author: Delario Nance, Jr.
"""

# Standard library imports
import numpy as np
import random
import sys

# Accessing project directories
from pathlib import Path # for adding filepaths
import sys # for adding filepaths

# Accessing project directories
FILEPATH_TO_SRC = str(Path(__file__)
                      .parent # path to folder of unit tests
                      .parent # path to folder of tests
                      .parent # path to project folder
                      / "src" # path to folder of data structures
                      )
sys.path.append(FILEPATH_TO_SRC)

# Local application imports
from ArrayList import ArrayList


def rand_arraylist(size: int, start: int = -1000, end: int = 1000) -> ArrayList:
    """Returns an ArrayList of a user-specified size, 
    containing random integers in the integer range
    [start, end].

    Args:
        size (int): The user-specified size
        start (int, optional): The start of the integer 
        range, inclusive. Defaults to -1000.
        end (int, optional): The end of the integer range,
        inclusive. Defaults to 1000.

    Returns:
        ArrayList: The ArrayList of random integers
    """
    
    random_values = [random.randint(start, end) for x in range(size)]
    return ArrayList(random_values)

def rand_ndarray(size: int, start: int = -1000, end: int = 1000):
    """Returns an NumPy array of a user-specified size, 
    containing random integers in the integer range
    [start, end].

    Args:
        size (int): The user-specified size
        start (int, optional): The start of the integer 
        range, inclusive. Defaults to -1000.
        end (int, optional): The end of the integer range,
        inclusive. Defaults to 1000.

    Returns:
        ArrayList: The ArrayList of random integers
    """
    
    random_values = np.random.randint(start, end+1, size)
    return random_values

def rand_pylist(size: int, start: int = -1000, end: int = 1000) -> list:
    """Returns an Pylist of a user-specified size, 
    containing random integers in the integer range
    [start, end].

    Args:
        size (int): The user-specified size
        start (int, optional): The start of the integer 
                               range, inclusive. Defaults to 
                               -1000.
        end (int, optional): The end of the integer range, 
                             inclusive. Defaults to 1000.

    Returns:
        list: The Pylist of random integers
    """
    
    random_values = [random.randint(start, end) for x in range(size)]
    return random_values
