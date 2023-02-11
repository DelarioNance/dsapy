"""
A Python script for integration testing the ArrayList class 
with PyTest.

Author: Delario Nance, Jr.
Date: January 24, 2023 - February 10, 2023
"""

# Standard library imports
import sys # for adding filepaths

# Accessing project directories
WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/BitBucket/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList
WSL_FILEPATH_TO_TESTING = "/home/delario-nance-jr/BitBucket/dsapy/testing" 
sys.path.append(WSL_FILEPATH_TO_TESTING) # helpers

# Local application imports
from ArrayList import ArrayList
from helpers import *


# Global variables
INDEX_BEFORE_NEWLINE = -1
TEST_RAN_WITHOUT_ERROR = True
DEFAULT_INT = 1729

class TestSettingValueWithCorrectNewValue:
    """Uses GettingValue and SettingValueWithoutError modules.
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


class TestAddingValueWithCorrectNewSize:
    """Uses AddingValueWithoutError and GettingSize modules.
    """
    def test_add_value_to_empty_ArrayList(self):
        empty_arraylist = rand_array_list(0)
        
        empty_arraylist.append(DEFAULT_INT)
        
        assert len(empty_arraylist) == 1
    
    def test_add_value_to_ArrayList_of_one_int(self):
        arraylist_of_one_int = rand_array_list(1)
        
        arraylist_of_one_int.append(DEFAULT_INT)
        
        assert len(arraylist_of_one_int) == 2
    
    def test_add_value_to_ArrayList_of_two_ints(self):
        arraylist_of_two_ints = rand_array_list(2)
        
        arraylist_of_two_ints.append(DEFAULT_INT)
        
        assert len(arraylist_of_two_ints) == 3
    
    def test_add_value_to_ArrayList_of_three_ints(self):
        arraylist_of_three_ints = rand_array_list(3)
        
        arraylist_of_three_ints.append(DEFAULT_INT)
        
        assert len(arraylist_of_three_ints) == 4
    
    def test_add_value_to_ArrayList_of_fifteen_ints(self):
        arraylist_of_fifteen_ints = rand_array_list(15)
        
        arraylist_of_fifteen_ints.append(DEFAULT_INT)
        
        assert len(arraylist_of_fifteen_ints) == 16
    
    def test_add_value_to_ArrayList_of_sixteen_ints(self):
        arraylist_of_sixteen_ints = rand_array_list(16)
        
        arraylist_of_sixteen_ints.append(DEFAULT_INT)
        
        assert len(arraylist_of_sixteen_ints) == 17
    
    def test_add_value_to_ArrayList_of_seventeen_ints(self):
        arraylist_of_seventeen_ints = rand_array_list(17)
        
        arraylist_of_seventeen_ints.append(DEFAULT_INT)
        
        assert len(arraylist_of_seventeen_ints) == 18
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
        
        arraylist_of_eight_thousand_one_hundred_ninety_one_ints.append(DEFAULT_INT)
        
        assert len(arraylist_of_eight_thousand_one_hundred_ninety_one_ints) == 8192
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
        
        arraylist_of_eight_thousand_one_hundred_ninety_two_ints.append(DEFAULT_INT)
        
        assert len(arraylist_of_eight_thousand_one_hundred_ninety_two_ints) == 8193
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
        
        arraylist_of_eight_thousand_one_hundred_ninety_three_ints.append(DEFAULT_INT)
        
        assert len(arraylist_of_eight_thousand_one_hundred_ninety_three_ints) == 8194
   
        
class TestAddingValueWithCorrectNewValue:
    """Uses AddingValueWithoutError and GettingValue modules.
    """
    def test_add_value_to_empty_ArrayList(self):
        empty_arraylist = rand_array_list(0)
        
        empty_arraylist.append(DEFAULT_INT)
        
        assert empty_arraylist[0] == DEFAULT_INT        
    
    def test_add_value_to_ArrayList_of_one_int(self):
        arraylist_of_one_int = rand_array_list(1)
        
        arraylist_of_one_int.append(DEFAULT_INT)
        
        assert arraylist_of_one_int[1] == DEFAULT_INT
    
    def test_add_value_to_ArrayList_of_two_ints(self):
        arraylist_of_two_ints = rand_array_list(2)
        
        arraylist_of_two_ints.append(DEFAULT_INT)
        
        assert arraylist_of_two_ints[2] == DEFAULT_INT
    
    def test_add_value_to_ArrayList_of_three_ints(self):
        arraylist_of_three_ints = rand_array_list(3)
        
        arraylist_of_three_ints.append(DEFAULT_INT)
        
        assert arraylist_of_three_ints[3] == DEFAULT_INT
    
    def test_add_value_to_ArrayList_of_fifteen_ints(self):
        arraylist_of_fifteen_ints = rand_array_list(15)
        
        arraylist_of_fifteen_ints.append(DEFAULT_INT)
        
        assert arraylist_of_fifteen_ints[15] == DEFAULT_INT
    
    def test_add_value_to_ArrayList_of_sixteen_ints(self):
        arraylist_of_sixteen_ints = rand_array_list(16)
        
        arraylist_of_sixteen_ints.append(DEFAULT_INT)
        
        assert arraylist_of_sixteen_ints[16] == DEFAULT_INT
    
    def test_add_value_to_ArrayList_of_seventeen_ints(self):
        arraylist_of_seventeen_ints = rand_array_list(17)
        
        arraylist_of_seventeen_ints.append(DEFAULT_INT)
        
        assert arraylist_of_seventeen_ints[17] == DEFAULT_INT
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
        
        arraylist_of_eight_thousand_one_hundred_ninety_one_ints.append(DEFAULT_INT)
        
        assert arraylist_of_eight_thousand_one_hundred_ninety_one_ints[8191] == DEFAULT_INT
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
        
        arraylist_of_eight_thousand_one_hundred_ninety_two_ints.append(DEFAULT_INT)
        
        assert arraylist_of_eight_thousand_one_hundred_ninety_two_ints[8192] == DEFAULT_INT
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
        
        arraylist_of_eight_thousand_one_hundred_ninety_three_ints.append(DEFAULT_INT)
        
        assert arraylist_of_eight_thousand_one_hundred_ninety_three_ints[8193] == DEFAULT_INT
        
        
        
class TestRemovingValueWithCorrectNewSize:
    """Uses RemovingValueWithoutError and GettingSize modules.
    """
    class TestRemovingValueFromArrayListOfOneInt:
        def test_remove_first_value_from_ArrayList_of_one_int(self):
            array_list_of_one_int = rand_array_list(1)
            
            array_list_of_one_int.remove(0)
            
            assert len(array_list_of_one_int) == 0
    
    
    class TestRemovingValueFromArrayListOfFifteenInts:
        def test_remove_first_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(0)
            
            assert len(array_list_of_fifteen_ints) == 14
        
        def test_remove_second_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(1)
            
            assert len(array_list_of_fifteen_ints) == 14
        
        def test_remove_middle_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(7)
            
            assert len(array_list_of_fifteen_ints) == 14
        
        def test_remove_penultimate_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(13)
            
            assert len(array_list_of_fifteen_ints) == 14

        def test_remove_last_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(14)
            
            assert len(array_list_of_fifteen_ints) == 14
    
    
    class TestRemovingValueFromArrayListOfSixteenInts:
        def test_remove_first_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(0)
            
            assert len(array_list_of_sixteen_ints) == 15
        
        def test_remove_second_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(1)
            
            assert len(array_list_of_sixteen_ints) == 15
        
        def test_remove_middle_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(7)
            
            assert len(array_list_of_sixteen_ints) == 15
        
        def test_remove_penultimate_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(14)
            
            assert len(array_list_of_sixteen_ints) == 15

        def test_remove_last_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(15)
            
            assert len(array_list_of_sixteen_ints) == 15
    
    
    class TestRemovingValueFromArrayListOfSeventeenInts:
        def test_remove_first_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(0)
            
            assert len(array_list_of_seventeen_ints) == 16
        
        def test_remove_second_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(1)
            
            assert len(array_list_of_seventeen_ints) == 16
        
        def test_remove_middle_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(8)
            
            assert len(array_list_of_seventeen_ints) == 16
        
        def test_remove_penultimate_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(15)
            
            assert len(array_list_of_seventeen_ints) == 16

        def test_remove_last_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(16)
            
            assert len(array_list_of_seventeen_ints) == 16
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyOneInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(0)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_one_ints) == 8190
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(1)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_one_ints) == 8190
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(4095)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_one_ints) == 8190
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(8189)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_one_ints) == 8190

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(8190)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_one_ints) == 8190
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyTwoInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(0)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_two_ints) == 8191
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(1)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_two_ints) == 8191
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(4095)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_two_ints) == 8191
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(8190)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_two_ints) == 8191

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(8191)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_two_ints) == 8191
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyThreeInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(0)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_three_ints) == 8192
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(1)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_three_ints) == 8192
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(4096)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_three_ints) == 8192
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(8191)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_three_ints) == 8192

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(8192)
            
            assert len(array_list_of_eight_thousand_one_hundred_ninety_three_ints) == 8192