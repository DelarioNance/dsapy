"""
A Python script for end-to-end testing the ArrayList class 
with PyTest.

Author: Delario Nance, Jr.
Date: February 15, 2023 - February 15, 2023
"""

# Standard library imports
import sys # for adding filepaths
import numpy as np

# Accessing project directories
WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/BitBucket/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList
WSL_FILEPATH_TO_TESTING = "/home/delario-nance-jr/BitBucket/dsapy/testing" 
sys.path.append(WSL_FILEPATH_TO_TESTING) # helpers

# Local application imports
from ArrayList import ArrayList
from helpers import *


class TestFindingMinimum:
    """Uses GettingValue and GettingSize modules.
    """
    def test_find_min_in_ArrayList_of_one_int(self):
        pylist_of_one_int = rand_pylist(1)
        arraylist_of_one_int = ArrayList(pylist_of_one_int)
        
        min_of_arraylist = arraylist_of_one_int.min()
        
        assert min_of_arraylist == min(pylist_of_one_int)
        
    def test_find_min_in_ArrayList_of_ten_ints(self):
        pylist_of_ten_ints = rand_pylist(10)
        arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
        
        min_of_arraylist = arraylist_of_ten_ints.min()
        
        assert min_of_arraylist == min(pylist_of_ten_ints)
        
    def test_find_min_in_ArrayList_of_one_hundred_ints(self):
        pylist_of_one_hundred_ints = rand_pylist(100)
        arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
        min_of_arraylist = arraylist_of_one_hundred_ints.min()
        
        assert min_of_arraylist == min(pylist_of_one_hundred_ints)
        
    def test_find_min_in_ArrayList_of_ten_thousand_ints(self):
        pylist_of_ten_thousand_ints = rand_pylist(10000)
        arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
        min_of_arraylist = arraylist_of_ten_thousand_ints.min()
        
        assert min_of_arraylist == min(pylist_of_ten_thousand_ints)
        
class TestFindingMaximum:
    """Uses GettingValue and GettingSize modules.
    """
    def test_find_max_in_ArrayList_of_one_int(self):
        pylist_of_one_int = rand_pylist(1)
        arraylist_of_one_int = ArrayList(pylist_of_one_int)
        
        max_of_arraylist = arraylist_of_one_int.max()
        
        assert max_of_arraylist == max(pylist_of_one_int)
        
    def test_find_max_in_ArrayList_of_ten_ints(self):
        pylist_of_ten_ints = rand_pylist(10)
        arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
        
        max_of_arraylist = arraylist_of_ten_ints.max()
        
        assert max_of_arraylist == max(pylist_of_ten_ints)
        
    def test_find_max_in_ArrayList_of_one_hundred_ints(self):
        pylist_of_one_hundred_ints = rand_pylist(100)
        arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
        max_of_arraylist = arraylist_of_one_hundred_ints.max()
        
        assert max_of_arraylist == max(pylist_of_one_hundred_ints)
        
    def test_find_max_in_ArrayList_of_ten_thousand_ints(self):
        pylist_of_ten_thousand_ints = rand_pylist(10000)
        arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
        max_of_arraylist = arraylist_of_ten_thousand_ints.max()
        
        assert max_of_arraylist == max(pylist_of_ten_thousand_ints)