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


class TestGettingSize:
    def test_get_size_of_empty_ArrayList(self):
        empty_arraylist = rand_array_list(0)
        size = len(empty_arraylist)
        assert size == 0
    
    def test_get_size_of_ArrayList_of_one_int(self):
        empty_arraylist = rand_array_list(1)
        size = len(empty_arraylist)
        assert size == 1
    
    def test_get_size_of_ArrayList_of_ten_ints(self):
        empty_arraylist = rand_array_list(10)
        size = len(empty_arraylist)
        assert size == 10
    
    def test_get_size_of_ArrayList_of_one_hundred_ints(self):
        empty_arraylist = rand_array_list(100)
        size = len(empty_arraylist)
        assert size == 100
    
    def test_get_size_of_ArrayList_of_ten_thousand_ints(self):
        empty_arraylist = rand_array_list(10000)
        size = len(empty_arraylist)
        assert size == 10000