"""
A Python script for unit testing the ArrayList class with 
PyTest.

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 28, 2023
"""

# Standard library imports
import numpy as np
import sys

# Accessing project directories
WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList
WSL_FILEPATH_TO_TESTING = "/home/delario-nance-jr/dsapy/testing" 
sys.path.append(WSL_FILEPATH_TO_TESTING) # helpers

# Local application imports
from ArrayList import ArrayList
from helpers import *

INDEX_BEFORE_NEWLINE = -1

class TestGettingSize:
    """Uses __init__ and __len__ methods from ArrayList class.
    """
    def test_get_size_of_empty_ArrayList(self):
        empty_arraylist = rand_array_list(0)
        
        size = len(empty_arraylist)
        
        assert size == 0
    
    def test_get_size_of_ArrayList_of_one_int(self):
        arraylist_of_one_int = rand_array_list(1)
        
        size = len(arraylist_of_one_int)
        
        assert size == 1
    
    def test_get_size_of_ArrayList_of_ten_ints(self):
        arraylist_of_ten_ints = rand_array_list(10)
        
        size = len(arraylist_of_ten_ints)
        
        assert size == 10
    
    def test_get_size_of_ArrayList_of_one_hundred_ints(self):
        arraylist_of_one_hundred_ints = rand_array_list(100)
        
        size = len(arraylist_of_one_hundred_ints)
        
        assert size == 100
    
    def test_get_size_of_ArrayList_of_ten_thousand_ints(self):
        arraylist_of_ten_thousand_ints = rand_array_list(10000)
        
        size = len(arraylist_of_ten_thousand_ints)
        
        assert size == 10000
        

class TestPrinting:
    """Uses __init__ and __str__ methods from ArrayList class.
    """
    def test_print_empty_ArrayList(self, capsys):
        empty_arraylist = rand_array_list(0)
        empty_ndarray = ndarray_of_first_ints(0)
        
        print(empty_arraylist)
        output_from_empty_arraylist = capsys.readouterr()[0][:INDEX_BEFORE_NEWLINE]
        
        assert output_from_empty_arraylist == str(empty_ndarray)
        
    
    def test_print_ArrayList_of_one_int(self, capsys):
        arraylist_of_one_int = array_list_range(1,1)
        ndarray_of_one_int = ndarray_of_first_ints(1)
        
        print(arraylist_of_one_int)
        output_from_arraylist_of_one_int = capsys.readouterr()[0][:INDEX_BEFORE_NEWLINE]
        
        assert output_from_arraylist_of_one_int == str(ndarray_of_one_int)
    
    def test_print_ArrayList_of_ten_ints(self, capsys):
        arraylist_of_ten_ints = array_list_range(1,10)
        ndarray_of_ten_ints = ndarray_of_first_ints(10)
        
        print(arraylist_of_ten_ints)
        output_from_arraylist_of_ten_ints = capsys.readouterr()[0][:INDEX_BEFORE_NEWLINE]
        
        assert output_from_arraylist_of_ten_ints == str(ndarray_of_ten_ints)
    
    def test_print_ArrayList_of_one_hundred_ints(self, capsys):
        arraylist_of_one_hundred_ints = array_list_range(1,100)
        ndarray_of_one_hundred_ints = ndarray_of_first_ints(100)
        
        print(arraylist_of_one_hundred_ints)
        output_from_arraylist_of_one_hundred_ints = capsys.readouterr()[0][:INDEX_BEFORE_NEWLINE]
        
        assert output_from_arraylist_of_one_hundred_ints == str(ndarray_of_one_hundred_ints)
    
    def test_print_ArrayList_of_ten_thousand_ints(self, capsys):
        arraylist_of_ten_thousand_ints = array_list_range(1,10000)
        ndarray_of_ten_thousand_ints = ndarray_of_first_ints(10000)
        
        print(arraylist_of_ten_thousand_ints)
        output_from_arraylist_of_ten_thousand_ints = capsys.readouterr()[0][:INDEX_BEFORE_NEWLINE]
        
        assert output_from_arraylist_of_ten_thousand_ints == str(ndarray_of_ten_thousand_ints)
        

class TestCheckingIfEmpty:
    """Uses __init__ and is_empty methods from ArrayList class.
    """
    def test_check_if_empty_ArrayList_is_empty(self):
        empty_arraylist = rand_array_list(0)
        
        verdict = empty_arraylist.is_empty()
        
        assert verdict == True
    
    def test_check_if_nonempty_ArrayList_is_empty(self):
        nonempty_arraylist = rand_array_list(1729)
        
        verdict = nonempty_arraylist.is_empty()
        
        assert verdict == False
        
        
class TestGettingValue:
    
    class TestGettingValueWithNonnegativeIndex:
        """Uses __init__ and __get_item__ methods from ArrayList class.
        """
        def test_get_first_value_in_ArrayList_of_one_ints_with_nonnegative_index(self):
            pylist_of_one_int = rand_pylist(1)
            arraylist_of_one_int = ArrayList(pylist_of_one_int)
            
            first_value_in_array_list = arraylist_of_one_int[0]
            
            assert first_value_in_array_list == pylist_of_one_int[0]
        
        
        def test_get_first_value_in_ArrayList_of_ten_ints_with_nonnegative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            first_value_in_array_list = arraylist_of_ten_ints[0]
            
            assert first_value_in_array_list == pylist_of_ten_ints[0]

        def test_get_second_value_in_ArrayList_of_ten_ints_with_nonnegative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            second_value_in_array_list = arraylist_of_ten_ints[1]
            
            assert second_value_in_array_list == pylist_of_ten_ints[1]
        
        def test_get_middle_value_in_ArrayList_of_ten_ints_with_nonnegative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            middle_value_in_array_list = arraylist_of_ten_ints[4]
            
            assert middle_value_in_array_list == pylist_of_ten_ints[4]

        def test_get_penultimate_value_in_ArrayList_of_ten_ints_with_nonnegative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            penultimate_value_in_array_list = arraylist_of_ten_ints[8]
            
            assert penultimate_value_in_array_list == pylist_of_ten_ints[8]
        
        def test_get_last_value_in_ArrayList_of_ten_ints_with_nonnegative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            last_value_in_array_list = arraylist_of_ten_ints[9]
            
            assert last_value_in_array_list == pylist_of_ten_ints[9]



        def test_get_first_value_in_ArrayList_of_one_hundred_ints_with_nonnegative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
            
            first_value_in_array_list = arraylist_of_one_hundred_ints[0]
            
            assert first_value_in_array_list == pylist_of_one_hundred_ints[0]
        
        def test_get_second_value_in_ArrayList_of_one_hundred_ints_with_nonnegative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
            second_value_in_array_list = arraylist_of_one_hundred_ints[1]
            
            assert second_value_in_array_list == pylist_of_one_hundred_ints[1]

        def test_get_middle_value_in_ArrayList_of_one_hundred_ints_with_nonnegative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
            middle_value_in_array_list = arraylist_of_one_hundred_ints[49]
            
            assert middle_value_in_array_list == pylist_of_one_hundred_ints[49]

        def test_get_penultimate_value_in_ArrayList_of_one_hundred_ints_with_nonnegative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
            penultimate_value_in_array_list = arraylist_of_one_hundred_ints[98]
            
            assert penultimate_value_in_array_list == pylist_of_one_hundred_ints[98]

        def test_get_last_value_in_ArrayList_of_one_hundred_ints_with_nonnegative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
            last_value_in_array_list = arraylist_of_one_hundred_ints[99]
            
            assert last_value_in_array_list == pylist_of_one_hundred_ints[99]


        def test_get_first_value_in_ArrayList_of_ten_thousand_ints_with_nonnegative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
            first_value_in_array_list = arraylist_of_ten_thousand_ints[0]
            
            assert first_value_in_array_list == pylist_of_ten_thousand_ints[0]

        def test_get_second_value_in_ArrayList_of_ten_thousand_ints_with_nonnegative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
            second_value_in_array_list = arraylist_of_ten_thousand_ints[1]
            
            assert second_value_in_array_list == pylist_of_ten_thousand_ints[1]

        def test_get_middle_value_in_ArrayList_of_ten_thousand_ints_with_nonnegative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
            middle_value_in_array_list = arraylist_of_ten_thousand_ints[4999]
            
            assert middle_value_in_array_list == pylist_of_ten_thousand_ints[4999]

        def test_get_penultimate_value_in_ArrayList_of_ten_thousand_ints_with_nonnegative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
            penultimate_value_in_array_list = arraylist_of_ten_thousand_ints[9998]
            
            assert penultimate_value_in_array_list == pylist_of_ten_thousand_ints[9998]

        def test_get_last_value_in_ArrayList_of_ten_thousand_ints_with_nonnegative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
            
            last_value_in_array_list = arraylist_of_ten_thousand_ints[9999]
            
            assert last_value_in_array_list == pylist_of_ten_thousand_ints[9999]