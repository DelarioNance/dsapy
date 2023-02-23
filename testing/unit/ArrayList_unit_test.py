"""
A Python script for unit testing the ArrayList class with 
PyTest.

Author: Delario Nance, Jr.
Date: January 24, 2023 - February 21, 2023
"""

# Standard library imports
import pytest # for markers
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
CAPACITY_MULTIPLE = 16
DEFAULT_INT = 1729
INDEX_BEFORE_NEWLINE = -1
STDOUT_INDEX = 0
TEST_RAN_WITHOUT_ERROR = True


class TestGettingSize:
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(0, id='zero_ints'),
        pytest.param(1, id='one_int'),
        pytest.param(10, id='ten_ints'),
        pytest.param(100, id='one_hundred_ints'),
        pytest.param(1000, id='one_thousand_ints'),
        pytest.param(10000, id='ten_thousand_ints')
    ])
    
    def test_get_size_of_ArrayList(self, num_of_ints) -> None:
        """Tests if a user can get the correct size of an 
        ArrayList of a user-specified number of random ints.

        Args:
            num_of_ints (_type_): The user-specified number 
            of random ints
        """
        arraylist = rand_arraylist(num_of_ints)
        
        size = len(arraylist)
        
        assert size == num_of_ints
        
        
class TestPrinting:
    """To test if ArrayList objects are correctly printed to 
    the command line, the test methods in this class take in
    the argument capsys - a built-in PyTest fixture which
    allows users to obtain the stdout/stderror data produced 
    when printing output to the command line.
    
    After calling capsys.readouterr(), the current data in
    stdout and stderror is returned as a tuple. To access the
    printed data (as a string with newline and tab 
    characters) in stdout, one can get the data at index 0 in
    the tuple returned by readouterr() as follows: 
        
        printed_output = capsys.readouterr()[0]
    
    Official PyTest documentation for capsys and other related fixtures in found in the [official PyTest documentation](https://docs.pytest.org/en/6.2.x/capture.html).
    
    The capsys tutorial used to familiarize myself with capsys can be is [this YouTube video](https://www.youtube.com/watch?v=dN-pVt7i4Us&t=215s) 
    by anthonywritescode. 
    """
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(0, id='zero_ints'),
        pytest.param(1, id='one_int'),
        pytest.param(10, id='ten_ints'),
        pytest.param(100, id='one_hundred_ints'),
        pytest.param(1000, id='one_thousand_ints'),
        pytest.param(10000, id='ten_thousand_ints')
    ])
    
    def test_print_ArrayList(self, capsys, num_of_ints: int) -> None:
        """Tests if a user can print the correct values in an
        ArrayList of a user-specified number of random ints.

        Args:
            capsys (_type_): The built-in pytest fixture for
            capturing stdout/stderror output
            num_of_ints (int): The user-specified number of 
            random ints
        """
        ndarray = rand_ndarray(num_of_ints)
        arraylist = ArrayList(ndarray)
        
        print(arraylist)
        printed_output = capsys.readouterr()[STDOUT_INDEX][:INDEX_BEFORE_NEWLINE]
        
        assert printed_output == str(ndarray)
        

class TestCheckingIfEmpty:
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(0, id='zero_ints'),
        pytest.param(1, id='one_int'),
        pytest.param(10, id='ten_ints'),
        pytest.param(100, id='one_hundred_ints'),
        pytest.param(1000, id='one_thousand_ints'),
        pytest.param(10000, id='ten_thousand_ints')
    ])
    
    def test_check_if_ArrayList_is_empty(self, num_of_ints: int) -> None:
        """Tests if a user can correctly determine if an 
        ArrayList of a user-specified number of random ints 
        is empty or not.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        arraylist = rand_arraylist(num_of_ints)
        
        verdict = arraylist.is_empty()
        
        assert verdict == (not num_of_ints) # not 0 = True
        
        
class TestGettingValue:
    class TestGettingValueWithNonnegativeIndex:
        @pytest.mark.parametrize("num_of_ints, index", [
            pytest.param(1,0, id="only value of one int"),
            pytest.param(10,0, id="start value of ten ints"),
            pytest.param(100,0, id="start value of one hundred ints"),
            pytest.param(1000,0, id="start value of one thousand ints"),
            pytest.param(10000,0, id="start value of ten thousand ints"),
            pytest.param(10,5, id="middle value of ten ints"),
            pytest.param(100,50, id="middle value of one hundred ints"),
            pytest.param(1000,500, id="middle value of one thousand ints"),
            pytest.param(10000,5000, id="middle value of ten thousand ints"),
            pytest.param(10,9, id="last value of ten ints"),
            pytest.param(100,99, id="last value of one hundred ints"),            
            pytest.param(1000,999, id="last value of one thousand ints"),          
            pytest.param(10000,9999, id="last value of ten thousand ints")
        ])
        
        def test_get_value_in_ArrayList_with_nonnegative_index(self, num_of_ints: int , index: int) -> None:
            """Tests if a user can get the correct value at
            a user-specified non-negative index in an ArrayList
            of a user-specified number of random ints.

            Args:
                num_of_ints (int): The user-specified number of
                random ints
                index (int): The user-specified index
            """
            pylist = rand_pylist(num_of_ints)
            arraylist = ArrayList(pylist)
            
            value = arraylist[index]
            
            assert value == pylist[index]
            
    class TestGettingValueWithNegativeIndex:
        @pytest.mark.parametrize("num_of_ints, index", [
            pytest.param(1,-1, id="only value of one int"),
            pytest.param(10,-10, id="start value of ten ints"),
            pytest.param(100,-100, id="start value of one hundred ints"),
            pytest.param(1000,-1000, id="start value of one thousand ints"),
            pytest.param(10000,-10000, id="start value of ten thousand ints"),
            pytest.param(10,-5, id="middle value of ten ints"),
            pytest.param(100,-50, id="middle value of one hundred ints"),
            pytest.param(1000,-500, id="middle value of one thousand ints"),
            pytest.param(10000,-5000, id="middle value of ten thousand ints"),
            pytest.param(10,-1, id="last value of ten ints"),
            pytest.param(100,-1, id="last value of one hundred ints"),            
            pytest.param(1000,-1, id="last value of one thousand ints"),          
            pytest.param(10000,-1, id="last value of ten thousand ints")
        ])
        
        def test_get_value_in_ArrayList_with_negative_index(self, num_of_ints: int , index: int) -> None:
            """Tests if a user can get the correct value at
            a user-specified negative index in an ArrayList
            of a user-specified number of random ints.

            Args:
                num_of_ints (int): The user-specified number of
                random ints
                index (int): The user-specified index
            """
            pylist = rand_pylist(num_of_ints)
            arraylist = ArrayList(pylist)
            
            value = arraylist[index]
            
            assert value == pylist[index]
                   
            
class TestSettingValueWithoutError:
    @pytest.mark.parametrize("num_of_ints, index", [
            pytest.param(1,-1, id="only value of one int"),
            pytest.param(10,-10, id="start value of ten ints"),
            pytest.param(100,-100, id="start value of one hundred ints"),
            pytest.param(1000,-1000, id="start value of one thousand ints"),
            pytest.param(10000,-10000, id="start value of ten thousand ints"),
            pytest.param(10,-5, id="middle value of ten ints"),
            pytest.param(100,-50, id="middle value of one hundred ints"),
            pytest.param(1000,-500, id="middle value of one thousand ints"),
            pytest.param(10000,-5000, id="middle value of ten thousand ints"),
            pytest.param(10,-1, id="last value of ten ints"),
            pytest.param(100,-1, id="last value of one hundred ints"),            
            pytest.param(1000,-1, id="last value of one thousand ints"),          
            pytest.param(10000,-1, id="last value of ten thousand ints")
        ])
    
    def test_set_value_in_ArrayList(self, num_of_ints: int, index: int) -> None:
        """Tests if a user can set a default value at a 
        user-specified non-negative index in an Array List
        of a user-specified number of random ints.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
            index (int): The user-specified index
        """
        arraylist = rand_arraylist(num_of_ints)
        
        arraylist[index] = DEFAULT_INT
        
        assert TEST_RAN_WITHOUT_ERROR
        

class TestAddingValueWithoutError:
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(0, id="zero ints"),
        pytest.param(CAPACITY_MULTIPLE * (2**0)-1, id="one int from full list of default capacity*(2^0)"),
        pytest.param(CAPACITY_MULTIPLE * (2**1)-1, id="one int from full list of default capacity*(2^1)"),
        pytest.param(CAPACITY_MULTIPLE * (2**4)-1, id="one int from full list of default capacity*(2^4)"),
        pytest.param(CAPACITY_MULTIPLE * (2**6)-1, id="one int from full list of default capacity*(2^6)"),
        pytest.param(CAPACITY_MULTIPLE * (2**8)-1, id="one int from full list of default capacity*(2^8)"),
        pytest.param(CAPACITY_MULTIPLE * (2**10)-1, id="one int from full list of default capacity*(2^10)"),
        pytest.param(CAPACITY_MULTIPLE * (2**0), id="full list of default capacity*(2^0)"),
        pytest.param(CAPACITY_MULTIPLE * (2**1), id="full list of default capacity*(2^1)"),
        pytest.param(CAPACITY_MULTIPLE * (2**4), id="full list of default capacity*(2^4)"),
        pytest.param(CAPACITY_MULTIPLE * (2**6), id="full list of default capacity*(2^6)"),
        pytest.param(CAPACITY_MULTIPLE * (2**8), id="full list of default capacity*(2^8)"),
        pytest.param(CAPACITY_MULTIPLE * (2**10), id="full list of default capacity*(2^10)"),
    ])
    
    def test_add_value_to_full_ArrayList(self, num_of_ints: int) -> None:
        """Tests if a user can add a default value to an 
        ArrayList of a user-specified number of random ints.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        arraylist = rand_arraylist(num_of_ints)
        
        arraylist.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
        
        
class TestRemovingValueWithoutError:
    """Uses __init__ and remove methods from ArrayList class.
    """
    class TestRemovingValueFromArrayListOfOneInt:
        def test_remove_first_value_from_ArrayList_of_one_int(self):
            array_list_of_one_int = rand_arraylist(1)
            
            array_list_of_one_int.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfFifteenInts:
        def test_remove_first_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_arraylist(15)
            
            array_list_of_fifteen_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_arraylist(15)
            
            array_list_of_fifteen_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_arraylist(15)
            
            array_list_of_fifteen_ints.remove(7)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_arraylist(15)
            
            array_list_of_fifteen_ints.remove(13)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_fifteen_ints(self):
            array_list_of_fifteen_ints = rand_arraylist(15)
            
            array_list_of_fifteen_ints.remove(14)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfSixteenInts:
        def test_remove_first_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_arraylist(16)
            
            array_list_of_sixteen_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_arraylist(16)
            
            array_list_of_sixteen_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_arraylist(16)
            
            array_list_of_sixteen_ints.remove(7)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_arraylist(16)
            
            array_list_of_sixteen_ints.remove(14)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_sixteen_ints(self):
            array_list_of_sixteen_ints = rand_arraylist(16)
            
            array_list_of_sixteen_ints.remove(15)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfSeventeenInts:
        def test_remove_first_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_arraylist(17)
            
            array_list_of_seventeen_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_arraylist(17)
            
            array_list_of_seventeen_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_arraylist(17)
            
            array_list_of_seventeen_ints.remove(8)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_arraylist(17)
            
            array_list_of_seventeen_ints.remove(15)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_seventeen_ints(self):
            array_list_of_seventeen_ints = rand_arraylist(17)
            
            array_list_of_seventeen_ints.remove(16)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyOneInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_arraylist(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_arraylist(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_arraylist(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(4095)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_arraylist(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(8189)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_one_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_one_ints = rand_arraylist(8191)
            
            array_list_of_eight_thousand_one_hundred_ninety_one_ints.remove(8190)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyTwoInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_arraylist(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_arraylist(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_arraylist(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(4095)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_arraylist(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(8190)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_two_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_two_ints = rand_arraylist(8192)
            
            array_list_of_eight_thousand_one_hundred_ninety_two_ints.remove(8191)
            
            assert TEST_RAN_WITHOUT_ERROR
    
    
    class TestRemovingValueFromArrayListOfEightThousandOneHundredNinetyThreeInts:
        def test_remove_first_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_arraylist(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_second_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_arraylist(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(1)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_middle_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_arraylist(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(4096)
            
            assert TEST_RAN_WITHOUT_ERROR
        
        def test_remove_penultimate_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_arraylist(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(8191)
            
            assert TEST_RAN_WITHOUT_ERROR

        def test_remove_last_value_from_ArrayList_of_eight_thousand_one_hundred_ninety_three_ints(self):
            array_list_of_eight_thousand_one_hundred_ninety_three_ints = rand_arraylist(8193)
            
            array_list_of_eight_thousand_one_hundred_ninety_three_ints.remove(8192)
            
            assert TEST_RAN_WITHOUT_ERROR