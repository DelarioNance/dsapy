"""
A Python script for unit testing the ArrayList class with 
PyTest.

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
    
    To test if ArrayList objects are correctly printed to the
    terminal, many of the unit test functions in the 
    TestPrinting class take in the argument capsys - a 
    built-in PyTest fixture which allows users to obtain the 
    stdout/stderror data produced when printing output.
    
    After calling capsys.readouterr(), the current data in
    stdout and stderror is returned as a tuple. To access the
    printed output (as a string with newline and tab 
    characters) in stdout, one can index the tuple returned
    by readouterr() as follows: 
        printed_output = capsys.readouterr()[0]
    
    Official PyTest documentation for capsys and other 
    related fixtures in found here: 
        https://docs.pytest.org/en/6.2.x/capture.html
    
    A tutorial of using capsys is found here: 
        https://www.youtube.com/watch?v=dN-pVt7i4Us&t=215s
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
        nonempty_arraylist = rand_array_list(DEFAULT_INT)
        
        verdict = nonempty_arraylist.is_empty()
        
        assert verdict == False
        
        
class TestGettingValue:
    """Uses __init__ and __get_item__ methods from ArrayList class.
    """
    
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
            
            
    class TestGettingValueWithNegativeIndex:
        """Uses __init__ and __get_item__ methods from ArrayList class.
        """
        def test_get_first_value_in_ArrayList_of_one_ints_with_negative_index(self):
            pylist_of_one_int = rand_pylist(1)
            arraylist_of_one_int = ArrayList(pylist_of_one_int)
            
            first_value_in_array_list = arraylist_of_one_int[-1]
            
            assert first_value_in_array_list == pylist_of_one_int[-1]
        
        
        def test_get_first_value_in_ArrayList_of_ten_ints_with_negative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            first_value_in_array_list = arraylist_of_ten_ints[-10]
            
            assert first_value_in_array_list == pylist_of_ten_ints[-10]

        def test_get_second_value_in_ArrayList_of_ten_ints_with_negative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            second_value_in_array_list = arraylist_of_ten_ints[-9]
            
            assert second_value_in_array_list == pylist_of_ten_ints[-9]
        
        def test_get_middle_value_in_ArrayList_of_ten_ints_with_negative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            middle_value_in_array_list = arraylist_of_ten_ints[-5]
            
            assert middle_value_in_array_list == pylist_of_ten_ints[-5]

        def test_get_penultimate_value_in_ArrayList_of_ten_ints_with_negative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            penultimate_value_in_array_list = arraylist_of_ten_ints[-2]
            
            assert penultimate_value_in_array_list == pylist_of_ten_ints[-2]
        
        def test_get_last_value_in_ArrayList_of_ten_ints_with_negative_index(self):
            pylist_of_ten_ints = rand_pylist(10)
            arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
            
            last_value_in_array_list = arraylist_of_ten_ints[-1]
            
            assert last_value_in_array_list == pylist_of_ten_ints[-1]



        def test_get_first_value_in_ArrayList_of_one_hundred_ints_with_negative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
            
            first_value_in_array_list = arraylist_of_one_hundred_ints[-100]
            
            assert first_value_in_array_list == pylist_of_one_hundred_ints[-100]
        
        def test_get_second_value_in_ArrayList_of_one_hundred_ints_with_negative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
            second_value_in_array_list = arraylist_of_one_hundred_ints[-99]
            
            assert second_value_in_array_list == pylist_of_one_hundred_ints[-99]

        def test_get_middle_value_in_ArrayList_of_one_hundred_ints_with_negative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
            middle_value_in_array_list = arraylist_of_one_hundred_ints[-50]
            
            assert middle_value_in_array_list == pylist_of_one_hundred_ints[-50]

        def test_get_penultimate_value_in_ArrayList_of_one_hundred_ints_with_negative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
            penultimate_value_in_array_list = arraylist_of_one_hundred_ints[-2]
            
            assert penultimate_value_in_array_list == pylist_of_one_hundred_ints[-2]

        def test_get_last_value_in_ArrayList_of_one_hundred_ints_with_negative_index(self):
            pylist_of_one_hundred_ints = rand_pylist(100)
            arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
            last_value_in_array_list = arraylist_of_one_hundred_ints[-1]
            
            assert last_value_in_array_list == pylist_of_one_hundred_ints[-1]


        def test_get_first_value_in_ArrayList_of_ten_thousand_ints_with_negative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
            first_value_in_array_list = arraylist_of_ten_thousand_ints[-10000]
            
            assert first_value_in_array_list == pylist_of_ten_thousand_ints[-10000]

        def test_get_second_value_in_ArrayList_of_ten_thousand_ints_with_negative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
            second_value_in_array_list = arraylist_of_ten_thousand_ints[-9999]
            
            assert second_value_in_array_list == pylist_of_ten_thousand_ints[-9999]

        def test_get_middle_value_in_ArrayList_of_ten_thousand_ints_with_negative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
            middle_value_in_array_list = arraylist_of_ten_thousand_ints[-5000]
            
            assert middle_value_in_array_list == pylist_of_ten_thousand_ints[-5000]

        def test_get_penultimate_value_in_ArrayList_of_ten_thousand_ints_with_negative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
            penultimate_value_in_array_list = arraylist_of_ten_thousand_ints[-2]
            
            assert penultimate_value_in_array_list == pylist_of_ten_thousand_ints[-2]

        def test_get_last_value_in_ArrayList_of_ten_thousand_ints_with_negative_index(self):
            pylist_of_ten_thousand_ints = rand_pylist(10000)
            arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
            
            last_value_in_array_list = arraylist_of_ten_thousand_ints[-1]
            
            assert last_value_in_array_list == pylist_of_ten_thousand_ints[-1]
                   
            
class TestSettingValueWithoutError:
    """Uses __init__ and __setitem__ methods from ArrayList class.
    """
    def test_set_value_at_middle_index_in_ArrayList_of_one_int(self):
        arraylist_of_one_int = rand_array_list(1)
        
        arraylist_of_one_int[0] = DEFAULT_INT
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_set_value_at_middle_index_in_ArrayList_of_ten_ints(self):
        arraylist_of_ten_ints = rand_array_list(10)
        
        arraylist_of_ten_ints[4] = DEFAULT_INT
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_set_value_at_middle_index_in_ArrayList_of_one_hundred_ints(self):
        arraylist_of_one_hundred_ints = rand_array_list(100)
        
        arraylist_of_one_hundred_ints[49] = DEFAULT_INT
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_set_value_at_middle_index_in_ArrayList_of_ten_thousand_ints(self):
        arraylist_of_ten_thousand_ints = rand_array_list(10000)
        
        arraylist_of_ten_thousand_ints[4999] = DEFAULT_INT
        
        assert TEST_RAN_WITHOUT_ERROR
        

class TestAddingValueWithoutError:
    """Uses __init__ and append methods from ArrayList class.
    """
    def test_add_value_to_empty_ArrayList(self):
        empty_arraylist = rand_array_list(0)
        
        empty_arraylist.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_one_int(self):
        arraylist_of_one_int = rand_array_list(1)
        
        arraylist_of_one_int.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_two_ints(self):
        arraylist_of_two_ints = rand_array_list(2)
        
        arraylist_of_two_ints.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_three_ints(self):
        arraylist_of_three_ints = rand_array_list(3)
        
        arraylist_of_three_ints.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
        arraylist_of_fifteen_ints = rand_array_list(15)
        
        arraylist_of_fifteen_ints.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_sixteen_ints(self):
        arraylist_of_sixteen_ints = rand_array_list(16)
        
        arraylist_of_sixteen_ints.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_seventeen_ints(self):
        arraylist_of_seventeen_ints = rand_array_list(17)
        
        arraylist_of_seventeen_ints.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
        
        arraylist_of_eight_thousand_one_hundred_ninety_one_ints.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
        
        arraylist_of_eight_thousand_one_hundred_ninety_two_ints.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
    
    def test_add_value_to_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
        arraylist_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
        
        arraylist_of_eight_thousand_one_hundred_ninety_three_ints.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
        
        
class TestRemovingValueWithoutError:
    """Uses __init__ and remove methods from ArrayList class.
    """
    class TestRemovingValueFromArrayListOfOneInt:
        def test_remove_first_value_from_ArrayList_of_one_int(self):
            array_list_of_one_int = rand_array_list(1)
            
            array_list_of_one_int.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfFifteenInts:
        def test_remove_first_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(7)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(13)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_array_list(15)
            
            array_list_of_fifteen_ints.remove(14)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfSixteenInts:
        def test_remove_first_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(7)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(14)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_array_list(16)
            
            array_list_of_sixteen_ints.remove(15)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfSeventeenInts:
        def test_remove_first_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(8)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(15)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_array_list(17)
            
            array_list_of_seventeen_ints.remove(16)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyOneInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(4095)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(8189)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_array_list(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(8190)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyTwoInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(4095)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(8190)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_array_list(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(8191)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyThreeInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(4096)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(8191)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_array_list(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(8192)
            
            assert TEST_RAN_WITHOUT_ERROR