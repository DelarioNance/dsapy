"""
A Python script for integration testing the ArrayList class 
with PyTest.

Author: Delario Nance, Jr.
Date: January 24, 2023 - February 5, 2023
"""

# Standard library imports
import sys # for adding filepaths

# Accessing project directories
WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList
WSL_FILEPATH_TO_TESTING = "/home/delario-nance-jr/dsapy/testing" 
sys.path.append(WSL_FILEPATH_TO_TESTING) # helpers

# Local application imports
from ArrayList import ArrayList
from helpers import *


# Global variables
INDEX_BEFORE_NEWLINE = -1
TEST_RAN_WITHOUT_ERROR = True
DEFAULT_INT = 1729

class TestSettingValueWithCorrectNewValue:
    """Uses __init__ and __setitem__ methods.
    
    Uses GettingValue and SettingValueWithoutError modules.
    """
    def test_set_value_in_ArrayList_of_one_int(self):
        arraylist_of_one_int = rand_array_list(1)
        
        for index in range(1):
            arraylist_of_one_int[index] = index + 1 # Uses __setitem__
            
        for index in range(1):
            assert arraylist_of_one_int[index] == index + 1 # Uses __getitem__
    
    def test_set_values_in_ArrayList_of_ten_ints(self):
        arraylist_of_ten_ints = rand_array_list(10)
        
        for index in range(10):
            arraylist_of_ten_ints[index] = index + 1 # Uses __setitem__
            
        for index in range(10):
            assert arraylist_of_ten_ints[index] == index + 1 # Uses __getitem__
    
    def test_set_values_in_ArrayList_of_one_hundred_ints(self):
        arraylist_of_one_hundred_ints = rand_array_list(100)
        
        for index in range(100):
            arraylist_of_one_hundred_ints[index] = index + 1 # Uses __setitem__
            
        for index in range(100):
            assert arraylist_of_one_hundred_ints[index] == index + 1 # Uses __getitem__
    
    def test_set_values_in_ArrayList_of_ten_thousand_ints(self):
        arraylist_of_ten_thousand_ints = rand_array_list(10000)
        
        for index in range(10000):
            arraylist_of_ten_thousand_ints[index] = index + 1 # Uses __setitem__
            
        for index in range(10000):
            assert arraylist_of_ten_thousand_ints[index] == index + 1 # Uses __getitem__