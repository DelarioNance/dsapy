"""
A Python program containing the definitions of helper 
functions used in the unit, integration, and end-to-end test
scripts for the ArrayList class.

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 27, 2023
"""

# Standard library imports
import numpy as np
import random
import sys

# Accessing project directories
WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/BitBucket/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList

# Local application imports
from ArrayList import ArrayList


def rand_array_list(size: int, start: int = -1000, end: int = 1000) -> ArrayList:
    """Returns an ArrayList of a user-specified size, 
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
        ArrayList: The ArrayList of random integers
    """
    
    random_values = [random.randint(start, end) for x in range(size)]
    return ArrayList(random_values)

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

def array_list_range(start: int, end: int) -> list[int]:
    """Returns an Arraylist of the ints in the integer range
       [start, end].

    Args:
        start (int): The start of the integer range, inclusive.
        end (int): The start of the integer range, inclusive.

    Returns:
        list[int]: The Arraylist of ints in the range
                   [start,end]
    """
    sequence_of_values = [x for x in range(start, end+1)]
    return ArrayList(sequence_of_values)

def ndarray_of_first_ints(n: int) -> np.ndarray:
    """Returns a one-dimensional NumPy array of the first n
    positive integers.

    Args:
        n (int): The number of the first positive integers
    """
    first_n_ints = np.array([x for x in range(1,n+1)])
    return first_n_ints