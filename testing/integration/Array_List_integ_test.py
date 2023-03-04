"""
A Python script for integration testing the ArrayList class 
with PyTest.

Author: Delario Nance, Jr.
Date: January 24, 2023 - February 12, 2023
"""

# Standard library imports
import sys # for adding filepaths
import numpy as np

# Accessing project directories
WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/BitBucket/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList
WSL_FILEPATH_TO_TESTING = "/home/delario-nance-jr/BitBucket/dsapy/testing" 
sys.path.append(WSL_FILEPATH_TO_TESTING) # helpers

# Related third part imports
import pytest # for markers

# Local application imports
from ArrayList import ArrayList
from helpers import *

# Global variables
DEFAULT_INT = 1729
DUMMY_NEGATIVE_INT = -2 # Not -1 because -1 is the dummy negative int for ArrayLists
INDEX_BEFORE_NEWLINE = -1
TEST_RAN_WITHOUT_ERROR = True


class TestSettingValueWithCorrectNewValue:
    """Uses GettingValue and SettingValueWithoutError modules.
    """
    @pytest.mark.parametrize("num_of_ints, index", [
            pytest.param(1,0, id="only value of one int"),
            pytest.param(10,0, id="start value of ten ints"),
            pytest.param(100,0, id="start value of one-hundred ints"),
            pytest.param(1000,0, id="start value of one-thousand ints"),
            pytest.param(10000,0, id="start value of ten-thousand ints"),
            pytest.param(10,5, id="middle value of ten ints"),
            pytest.param(100,50, id="middle value of one-hundred ints"),
            pytest.param(1000,500, id="middle value of one-thousand ints"),
            pytest.param(10000,5000, id="middle value of ten-thousand ints"),
            pytest.param(10,9, id="last value of ten ints"),
            pytest.param(100,99, id="last value of one-hundred ints"),            
            pytest.param(1000,999, id="last value of one-thousand ints"),          
            pytest.param(10000,9999, id="last value of ten-thousand ints")
        ])
    
    def test_set_value_in_ArrayList(self, num_of_ints: int, index: int) -> None:
        """Tests if a user can set a default value at a 
        user-specified non-negative index in an Array List
        of a user-specified number of random ints, with the
        correct value.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
            index (int): The user-specified non-negative index
        """
        arraylist = rand_arraylist(num_of_ints)
        
        arraylist[index] = DEFAULT_INT
        
        assert arraylist[index] == DEFAULT_INT


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
       
            
class TestCheckingIfEqual:
    """In the TestCheckingIfEqualForSameSizeButDifferentValues 
    class for ensuring that ArrayLists of the same size but 
    with different values are considered unequal, my choice of
    using random values for our ArrayLists could
    theoretically produce ArrayLists with the same values
    (hence equal ArrayLists). However, since we are using 
    random integers in the range [-1000,1000], the 
    probability of since an event happening is equal to the
    fraction 1/(2001^n), where is the size of both ArrayLists.
    This fraction takes on a minimum value less than 0.05%
    (when n=1), so we will use random integers in the
    TestCheckingIfEqualForSameSizeButDifferentValues class.
    """
    class TestCheckingIfEqualForSameSizeAndSameValues:
        def test_check_if_empty_ArrayLists_are_equal(self):
            empty_pylist = []
            first_empty_arraylist = ArrayList(empty_pylist)
            second_empty_arraylist = ArrayList(empty_pylist)
            
            verdict = (first_empty_arraylist == second_empty_arraylist)
            
            assert verdict == True
            
        def test_check_if_equal_ArrayLists_of_one_int_are_equal(self):
            pylist_of_one_int = rand_pylist(1)
            first_arraylist_of_one_int = ArrayList(pylist_of_one_int)
            second_arraylist_of_one_int = ArrayList(pylist_of_one_int)
            
            verdict = (first_arraylist_of_one_int == second_arraylist_of_one_int)
            
            assert verdict == True
        
        def test_check_if_equal_ArrayLists_of_sixteen_ints_are_equal(self):
            pylist_of_sixteen_ints = rand_pylist(16)
            first_arraylist_of_sixteen_ints = ArrayList(pylist_of_sixteen_ints)
            second_arraylist_of_sixteen_ints = ArrayList(pylist_of_sixteen_ints)
            
            verdict = (first_arraylist_of_sixteen_ints == second_arraylist_of_sixteen_ints)
            
            assert verdict == True
        
        def test_check_if_equal_ArrayLists_of_one_int_are_equal(self):
            pylist_of_one_thousand_two_hundred_twenty_nine_ints = rand_pylist(DEFAULT_INT)
            first_arraylist_of_one_thousand_two_hundred_twenty_nine_ints = ArrayList(pylist_of_one_thousand_two_hundred_twenty_nine_ints)
            second_arraylist_of_one_thousand_two_hundred_twenty_nine_ints = ArrayList(pylist_of_one_thousand_two_hundred_twenty_nine_ints)
            
            verdict = (first_arraylist_of_one_thousand_two_hundred_twenty_nine_ints == second_arraylist_of_one_thousand_two_hundred_twenty_nine_ints)
            
            assert verdict == True
    
    
    class TestCheckingIfEqualForSameSizeButDifferentValues:
        def test_check_if_ArrayLists_of_one_int_but_different_values_are_equal(self):
            first_arraylist_of_one_int =  rand_array_list(1)
            second_arraylist_of_one_int = rand_array_list(1)
            
            verdict = (first_arraylist_of_one_int == second_arraylist_of_one_int)
            
            assert verdict == False                
        
        def test_check_if_ArrayLists_of_sixteen_ints_but_different_values_are_equal(self):
            first_arraylist_of_sixteen_ints =  rand_array_list(16)
            second_arraylist_of_sixteen_ints = rand_array_list(16)
            
            verdict = (first_arraylist_of_sixteen_ints == second_arraylist_of_sixteen_ints)
            
            assert verdict == False   
        
        def test_check_if_ArrayLists_of_one_thousand_two_hundred_twenty_nine_ints_but_different_values_are_equal(self):
            first_arraylist_of_one_thousand_two_hundred_twenty_nine_ints =  rand_array_list(DEFAULT_INT)
            second_arraylist_of_one_thousand_two_hundred_twenty_nine_ints = rand_array_list(DEFAULT_INT)
            
            verdict = (first_arraylist_of_one_thousand_two_hundred_twenty_nine_ints == second_arraylist_of_one_thousand_two_hundred_twenty_nine_ints)
            
            assert verdict == False   
    
    
    class TestCheckingIfEqualForSameValuesButDifferentSizes:
        def test_check_if_ArrayLists_of_same_one_int_but_different_sizes_are_equal(self):
            pylist_of_one_int = rand_pylist(1)
            arraylist_of_one_int = ArrayList(pylist_of_one_int)
            arraylist_of_two_ints = ArrayList(pylist_of_one_int + [DUMMY_NEGATIVE_INT])
            
            verdict = (arraylist_of_one_int == arraylist_of_two_ints)
            
            assert verdict == False
        
        def test_check_if_ArrayLists_of_same_sixteen_ints_but_different_sizes_are_equal(self):
            pylist_of_sixteen_ints = rand_pylist(16)
            arraylist_of_sixteen_ints = ArrayList(pylist_of_sixteen_ints)
            arraylist_of_seventeen_ints = ArrayList(pylist_of_sixteen_ints + [DUMMY_NEGATIVE_INT])
            
            verdict = (arraylist_of_sixteen_ints == arraylist_of_seventeen_ints)
            
            assert verdict == False
        
        def test_check_if_ArrayLists_of_same_one_thousand_two_hundred_twenty_nine_ints_but_different_sizes_are_equal(self):
            pylist_of_one_thousand_two_hundred_twenty_nine_ints = rand_pylist(DEFAULT_INT)
            arraylist_of_one_thousand_two_hundred_twenty_nine_ints = ArrayList(pylist_of_one_thousand_two_hundred_twenty_nine_ints)
            arraylist_of_one_thousand_two_hundred_thirty_ints = ArrayList(pylist_of_one_thousand_two_hundred_twenty_nine_ints + [DUMMY_NEGATIVE_INT])
            
            verdict = (arraylist_of_one_thousand_two_hundred_twenty_nine_ints == arraylist_of_one_thousand_two_hundred_thirty_ints)
            
            assert verdict == False
    
    
    class TestCheckingIfEqualForDifferentSizeAndDifferentValues:
        def test_check_if_ArrayLists_of_different_size_and_different_ints_are_equal(self):
            arraylist_of_one_int =  rand_array_list(1)
            arraylist_of_two_ints = rand_array_list(2)
            
            verdict = (arraylist_of_one_int == arraylist_of_two_ints)
            
            assert verdict == False
        
        def test_check_if_ArrayLists_of_different_size_and_different_ints_are_equal(self):
            arraylist_of_sixteen_ints =  rand_array_list(16)
            arraylist_of_seventeen_ints = rand_array_list(17)
            
            verdict = (arraylist_of_sixteen_ints == arraylist_of_seventeen_ints)
            
            assert verdict == False
        
        def test_check_if_ArrayLists_of_different_size_and_different_ints_are_equal(self):
            arraylist_of_one_thousand_two_hundred_twenty_nine_ints =  rand_array_list(1229)
            arraylist_of_one_thousand_two_hundred_thirty_ints = rand_array_list(1230)
            
            verdict = (arraylist_of_one_thousand_two_hundred_twenty_nine_ints == arraylist_of_one_thousand_two_hundred_thirty_ints)
            
            assert verdict == False
    
            
class TestRemovingValueWithCorrectOldValues:
    """Uses RemovingValueWithoutError module.
    """
    class TestRemovingValueFromArrayListOfOneInt:
        def test_remove_first_value_from_ArrayList_of_one_int(self):
            pylist_of_one_int = rand_pylist(1)
            array_list_of_one_int = ArrayList(pylist_of_one_int)
            
            array_list_of_one_int.remove(0)
            verdict = np.array_equal(array_list_of_one_int._values[:0], pylist_of_one_int[1:])
            
            assert verdict == True
    
    
    class TestRemovingValueFromArrayListOfFifteenInts:
        def test_remove_first_value_from_ArrayList_of_fifteen_ints(self):
            index_after_removed = 1
            pylist_of_fifteen_ints = rand_pylist(15)
            array_list_of_fifteen_ints = ArrayList(pylist_of_fifteen_ints)
            
            array_list_of_fifteen_ints.remove(0)
            verdict = np.array_equal(array_list_of_fifteen_ints._values[:14], pylist_of_fifteen_ints[:index_after_removed-1]+pylist_of_fifteen_ints[index_after_removed:])
            
            assert verdict == True
          
        def test_remove_second_value_from_ArrayList_of_fifteen_ints(self):
            index_after_removed = 2
            pylist_of_fifteen_ints = rand_pylist(15)
            array_list_of_fifteen_ints = ArrayList(pylist_of_fifteen_ints)
            
            array_list_of_fifteen_ints.remove(1)
            verdict = np.array_equal(array_list_of_fifteen_ints._values[:14], pylist_of_fifteen_ints[:index_after_removed-1]+pylist_of_fifteen_ints[index_after_removed:])

            assert verdict == True
            
        def test_remove_middle_value_from_ArrayList_of_fifteen_ints(self):
            index_after_removed = 8
            pylist_of_fifteen_ints = rand_pylist(15)
            array_list_of_fifteen_ints = ArrayList(pylist_of_fifteen_ints)
            
            array_list_of_fifteen_ints.remove(7)
            verdict = np.array_equal(array_list_of_fifteen_ints._values[:14], pylist_of_fifteen_ints[:index_after_removed-1]+pylist_of_fifteen_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_penultimate_value_from_ArrayList_of_fifteen_ints(self):
            index_after_removed = 14
            pylist_of_fifteen_ints = rand_pylist(15)
            array_list_of_fifteen_ints = ArrayList(pylist_of_fifteen_ints)
            
            array_list_of_fifteen_ints.remove(13)
            verdict = np.array_equal(array_list_of_fifteen_ints._values[:14], pylist_of_fifteen_ints[:index_after_removed-1]+pylist_of_fifteen_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_last_value_from_ArrayList_of_fifteen_ints(self):
            index_after_removed = 15
            pylist_of_fifteen_ints = rand_pylist(15)
            array_list_of_fifteen_ints = ArrayList(pylist_of_fifteen_ints)
            
            array_list_of_fifteen_ints.remove(14)
            verdict = np.array_equal(array_list_of_fifteen_ints._values[:14], pylist_of_fifteen_ints[:index_after_removed-1]+pylist_of_fifteen_ints[index_after_removed:])
            
            assert verdict == True
            
    
    class TestRemovingValueFromArrayListOfSixteenInts:
        def test_remove_first_value_from_ArrayList_of_sixteen_ints(self):
            index_after_removed = 1
            pylist_of_sixteen_ints = rand_pylist(16)
            array_list_of_sixteen_ints = ArrayList(pylist_of_sixteen_ints)
            
            array_list_of_sixteen_ints.remove(0)
            verdict = np.array_equal(array_list_of_sixteen_ints._values[:15], pylist_of_sixteen_ints[:index_after_removed-1]+pylist_of_sixteen_ints[index_after_removed:])
            
            assert verdict == True
          
        def test_remove_second_value_from_ArrayList_of_sixteen_ints(self):
            index_after_removed = 2
            pylist_of_sixteen_ints = rand_pylist(16)
            array_list_of_sixteen_ints = ArrayList(pylist_of_sixteen_ints)
            
            array_list_of_sixteen_ints.remove(1)
            verdict = np.array_equal(array_list_of_sixteen_ints._values[:15], pylist_of_sixteen_ints[:index_after_removed-1]+pylist_of_sixteen_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_middle_value_from_ArrayList_of_sixteen_ints(self):
            index_after_removed = 8
            pylist_of_sixteen_ints = rand_pylist(16)
            array_list_of_sixteen_ints = ArrayList(pylist_of_sixteen_ints)
            
            array_list_of_sixteen_ints.remove(7)
            verdict = np.array_equal(array_list_of_sixteen_ints._values[:15], pylist_of_sixteen_ints[:index_after_removed-1]+pylist_of_sixteen_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_penultimate_value_from_ArrayList_of_sixteen_ints(self):
            index_after_removed = 15
            pylist_of_sixteen_ints = rand_pylist(16)
            array_list_of_sixteen_ints = ArrayList(pylist_of_sixteen_ints)
            
            array_list_of_sixteen_ints.remove(14)
            verdict = np.array_equal(array_list_of_sixteen_ints._values[:15], pylist_of_sixteen_ints[:index_after_removed-1]+pylist_of_sixteen_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_last_value_from_ArrayList_of_sixteen_ints(self):
            index_after_removed = 16
            pylist_of_sixteen_ints = rand_pylist(16)
            array_list_of_sixteen_ints = ArrayList(pylist_of_sixteen_ints)
            
            array_list_of_sixteen_ints.remove(15)
            verdict = np.array_equal(array_list_of_sixteen_ints._values[:15], pylist_of_sixteen_ints[:index_after_removed-1]+pylist_of_sixteen_ints[index_after_removed:])
            
            assert verdict == True
    
    
    class TestRemovingValueFromArrayListOfSeventeenInts:
        def test_remove_first_value_from_ArrayList_of_seventeen_ints(self):
            index_after_removed = 1
            pylist_of_seventeen_ints = rand_pylist(17)
            array_list_of_seventeen_ints = ArrayList(pylist_of_seventeen_ints)
            
            array_list_of_seventeen_ints.remove(0)
            verdict = np.array_equal(array_list_of_seventeen_ints._values[:16], pylist_of_seventeen_ints[:index_after_removed-1]+pylist_of_seventeen_ints[index_after_removed:])
            
            assert verdict == True
          
        def test_remove_second_value_from_ArrayList_of_seventeen_ints(self):
            index_after_removed = 2
            pylist_of_seventeen_ints = rand_pylist(17)
            array_list_of_seventeen_ints = ArrayList(pylist_of_seventeen_ints)
            
            array_list_of_seventeen_ints.remove(1)
            verdict = np.array_equal(array_list_of_seventeen_ints._values[:16], pylist_of_seventeen_ints[:index_after_removed-1]+pylist_of_seventeen_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_middle_value_from_ArrayList_of_seventeen_ints(self):
            index_after_removed = 9
            pylist_of_seventeen_ints = rand_pylist(17)
            array_list_of_seventeen_ints = ArrayList(pylist_of_seventeen_ints)
            
            array_list_of_seventeen_ints.remove(8)
            verdict = np.array_equal(array_list_of_seventeen_ints._values[:16], pylist_of_seventeen_ints[:index_after_removed-1]+pylist_of_seventeen_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_penultimate_value_from_ArrayList_of_seventeen_ints(self):
            index_after_removed = 16
            pylist_of_seventeen_ints = rand_pylist(17)
            array_list_of_seventeen_ints = ArrayList(pylist_of_seventeen_ints)
            
            array_list_of_seventeen_ints.remove(15)
            verdict = np.array_equal(array_list_of_seventeen_ints._values[:16], pylist_of_seventeen_ints[:index_after_removed-1]+pylist_of_seventeen_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_last_value_from_ArrayList_of_seventeen_ints(self):
            index_after_removed = 17
            pylist_of_seventeen_ints = rand_pylist(17)
            array_list_of_seventeen_ints = ArrayList(pylist_of_seventeen_ints)
            
            array_list_of_seventeen_ints.remove(16)
            verdict = np.array_equal(array_list_of_seventeen_ints._values[:16], pylist_of_seventeen_ints[:index_after_removed-1]+pylist_of_seventeen_ints[index_after_removed:])
            
            assert verdict == True
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyOneInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            index_after_removed = 1
            pylist_of_eight_thousand_one_hundred_ninety_one_ints = rand_pylist(8191)
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_one_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(0)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_one_ints._values[:8190], pylist_of_eight_thousand_one_hundred_ninety_one_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_one_ints[index_after_removed:])
            
            assert verdict == True
          
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            index_after_removed = 2
            pylist_of_eight_thousand_one_hundred_ninety_one_ints = rand_pylist(8191)
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_one_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(1)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_one_ints._values[:8190], pylist_of_eight_thousand_one_hundred_ninety_one_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_one_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            index_after_removed = 4096
            pylist_of_eight_thousand_one_hundred_ninety_one_ints = rand_pylist(8191)
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_one_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(4095)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_one_ints._values[:8190], pylist_of_eight_thousand_one_hundred_ninety_one_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_one_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            index_after_removed = 8190
            pylist_of_eight_thousand_one_hundred_ninety_one_ints = rand_pylist(8191)
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_one_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(8189)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_one_ints._values[:8190], pylist_of_eight_thousand_one_hundred_ninety_one_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_one_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            index_after_removed = 8191
            pylist_of_eight_thousand_one_hundred_ninety_one_ints = rand_pylist(8191)
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_one_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(8190)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_one_ints._values[:8190], pylist_of_eight_thousand_one_hundred_ninety_one_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_one_ints[index_after_removed:])
            
            assert verdict == True
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyTwoInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            index_after_removed = 1
            pylist_of_eight_thousand_one_hundred_ninety_two_ints = rand_pylist(8192)
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_two_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(0)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_two_ints._values[:8191], pylist_of_eight_thousand_one_hundred_ninety_two_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_two_ints[index_after_removed:])
            
            assert verdict == True
          
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            index_after_removed = 2
            pylist_of_eight_thousand_one_hundred_ninety_two_ints = rand_pylist(8192)
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_two_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(1)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_two_ints._values[:8191], pylist_of_eight_thousand_one_hundred_ninety_two_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_two_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            index_after_removed = 4096
            pylist_of_eight_thousand_one_hundred_ninety_two_ints = rand_pylist(8192)
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_two_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(4095)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_two_ints._values[:8191], pylist_of_eight_thousand_one_hundred_ninety_two_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_two_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            index_after_removed = 8191
            pylist_of_eight_thousand_one_hundred_ninety_two_ints = rand_pylist(8192)
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_two_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(8190)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_two_ints._values[:8191], pylist_of_eight_thousand_one_hundred_ninety_two_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_two_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            index_after_removed = 8192
            pylist_of_eight_thousand_one_hundred_ninety_two_ints = rand_pylist(8192)
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_two_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(8191)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_two_ints._values[:8191], pylist_of_eight_thousand_one_hundred_ninety_two_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_two_ints[index_after_removed:])
            
            assert verdict == True
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyThreeInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            index_after_removed = 1
            pylist_of_eight_thousand_one_hundred_ninety_three_ints = rand_pylist(8193)
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_three_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(0)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_three_ints._values[:8192], pylist_of_eight_thousand_one_hundred_ninety_three_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_three_ints[index_after_removed:])
            
            assert verdict == True
          
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            index_after_removed = 2
            pylist_of_eight_thousand_one_hundred_ninety_three_ints = rand_pylist(8193)
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_three_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(1)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_three_ints._values[:8192], pylist_of_eight_thousand_one_hundred_ninety_three_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_three_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            index_after_removed = 4097
            pylist_of_eight_thousand_one_hundred_ninety_three_ints = rand_pylist(8193)
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_three_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(4096)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_three_ints._values[:8192], pylist_of_eight_thousand_one_hundred_ninety_three_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_three_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            index_after_removed = 8192
            pylist_of_eight_thousand_one_hundred_ninety_three_ints = rand_pylist(8193)
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_three_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(8191)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_three_ints._values[:8192], pylist_of_eight_thousand_one_hundred_ninety_three_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_three_ints[index_after_removed:])
            
            assert verdict == True
            
        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            index_after_removed = 8193
            pylist_of_eight_thousand_one_hundred_ninety_three_ints = rand_pylist(8193)
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = ArrayList(pylist_of_eight_thousand_one_hundred_ninety_three_ints)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(8192)
            verdict = np.array_equal(array_list_of_eight_thousand_one_hundred_ninety_three_ints._values[:8192], pylist_of_eight_thousand_one_hundred_ninety_three_ints[:index_after_removed-1]+pylist_of_eight_thousand_one_hundred_ninety_three_ints[index_after_removed:])
            
            assert verdict == True