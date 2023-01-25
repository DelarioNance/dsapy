"""
A Python program containing the definitions of helper 
functions used in the unit, integration, and end-to-end test
scripts for the ArrayList class.

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 24, 2023
"""

FILEPATH_TO_SRC = "c:\\Users\\Delar\\OneDrive\\Desktop\\Winter Break\\Repos\\DSAPy\\dsapy\\src"

import sys
sys.path.append(FILEPATH_TO_SRC)

from ArrayList import ArrayList
import random

def rand_array_list(size: int, start: int = -1000, end: int = 1000) -> ArrayList:
    """Returns an ArrayList of a user-specified size, 
    containing random integers in a user-specified range 
    [start,end).

    Args:
        size (int): specified
        start (int, optional): The start of the random range, 
                               inclusive. Defaults to -1000.
        end (int, optional): The end of the random range, 
                             inclusive. Defaults to 1000.

    Returns:
        ArrayList: The ArrayList of random integers
    """
    
    random_values = [random.randint(start, end) for x in range(size)]
    return ArrayList(random_values)