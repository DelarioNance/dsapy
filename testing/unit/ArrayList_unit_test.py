"""
A Python script for unit testing the ArrayList class with 
PyTest.

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 27, 2023
"""

# Standard library imports
import sys

# Accessing project directories
WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList
WSL_FILEPATH_TO_TESTING = "/home/delario-nance-jr/dsapy/testing" 
sys.path.append(WSL_FILEPATH_TO_TESTING) # helpers

# Local application imports
from ArrayList import ArrayList
from helpers import rand_array_list


class testGettingSize:
    def test_get_size_of_empty_ArrayList(self):

        empty_arraylist = ArrayList()
        size = len(empty_arraylist)
        assert size == 0