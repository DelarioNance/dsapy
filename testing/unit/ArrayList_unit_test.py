"""
A Python script for unit testing the ArrayList class with 
Pytest.

Author: Delario Nance, Jr.
Date: January 24, 2023 - February 25, 2023
"""

# Standard library imports
import sys # for adding filepaths

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
DEFAULT_CAPACITY = 16
DEFAULT_INT = 1729
INDEX_BEFORE_NEWLINE = -1
STDOUT_INDEX = 0
TEST_RAN_WITHOUT_ERROR = True


class TestGettingSize:
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(0, id='zero ints'),
        pytest.param(1, id='one int'),
        pytest.param(10, id='ten ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(1000, id='one-thousand ints'),
        pytest.param(10000, id='ten-thousand ints')
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
    the argument capsys - a built-in Pytest fixture which
    lets users obtain the stdout/stderror data produced 
    when printing output to the command line.
    
    After calling capsys.readouterr(), the current data in
    stdout and stderror is returned as a tuple. To access the
    printed data (as a string with newline and tab 
    characters) from stdout, one index the tuple returned by 
    readouterr() as follows: 
        
        printed_output = capsys.readouterr()[0]
    
    Official Pytest documentation for capsys and other related fixtures are found in the [official PyTest documentation](https://docs.pytest.org/en/6.2.x/capture.html).
    
    The tutorial used to familiarize myself with capsys is this [YouTube video](https://www.youtube.com/watch?v=dN-pVt7i4Us&t=215s) 
    by anthonywritescode. 
    """
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(0, id='zero ints'),
        pytest.param(1, id='one int'),
        pytest.param(10, id='ten ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(1000, id='one-thousand ints'),
        pytest.param(10000, id='ten-thousand ints')
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
        # capsys is used to get the printed output
        # of the ArrayList instead of __str__ because
        # the __str__ method might be replaced with a 
        # different method (e.g., __repr__) in the 
        # ArrayList class
        ndarray = rand_ndarray(num_of_ints)
        arraylist = ArrayList(ndarray)
        
        print(arraylist)
        printed_output = capsys.readouterr()[STDOUT_INDEX][:INDEX_BEFORE_NEWLINE]
        
        assert printed_output == str(ndarray)
        
        
class TestGettingValue:
    class TestGettingValueWithNonnegativeIndex:
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
        
        def test_get_value_in_ArrayList_with_nonnegative_index(self, num_of_ints: int , index: int) -> None:
            """Tests if a user can get the correct value at
            a user-specified non-negative index in an ArrayList
            of a user-specified number of random ints.

            Args:
                num_of_ints (int): The user-specified number of
                random ints
                index (int): The user-specified non-negative
                index
            """
            pylist = rand_pylist(num_of_ints)
            arraylist = ArrayList(pylist)
            
            value = arraylist[index]
            
            assert value == pylist[index]
            
            
    class TestGettingValueWithNegativeIndex:
        @pytest.mark.parametrize("num_of_ints, index", [
            pytest.param(1,-1, id="only value of one int"),
            pytest.param(10,-10, id="start value of ten ints"),
            pytest.param(100,-100, id="start value of one-hundred ints"),
            pytest.param(1000,-1000, id="start value of one-thousand ints"),
            pytest.param(10000,-10000, id="start value of ten-thousand ints"),
            pytest.param(10,-5, id="middle value of ten ints"),
            pytest.param(100,-50, id="middle value of one-hundred ints"),
            pytest.param(1000,-500, id="middle value of one-thousand ints"),
            pytest.param(10000,-5000, id="middle value of ten-thousand ints"),
            pytest.param(10,-1, id="last value of ten ints"),
            pytest.param(100,-1, id="last value of one-hundred ints"),            
            pytest.param(1000,-1, id="last value of one-thousand ints"),          
            pytest.param(10000,-1, id="last value of ten-thousand ints")
        ])
        
        def test_get_value_in_ArrayList_with_negative_index(self, num_of_ints: int , index: int) -> None:
            """Tests if a user can get the correct value at
            a user-specified negative index in an ArrayList
            of a user-specified number of random ints.

            Args:
                num_of_ints (int): The user-specified number of
                random ints
                index (int): The user-specified negative index
            """
            pylist = rand_pylist(num_of_ints)
            arraylist = ArrayList(pylist)
            
            value = arraylist[index]
            
            assert value == pylist[index]
                   
            
class TestSettingValueWithoutError:
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
        of a user-specified number of random ints, without
        error.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
            index (int): The user-specified non-negative index
        """
        arraylist = rand_arraylist(num_of_ints)
        
        arraylist[index] = DEFAULT_INT
        
        assert TEST_RAN_WITHOUT_ERROR
        

class TestAppendingValueWithoutError:
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(0, id="list of zero ints"),
        pytest.param(1, id="list of one int"),
        pytest.param(2, id="list of two ints"),
        pytest.param(DEFAULT_CAPACITY*(2**0)-1, id="one-from-full list of default_capacity*(2^0)-1"),
        pytest.param(DEFAULT_CAPACITY*(2**2)-1, id="one-from-full list of default_capacity*(2^2)-1"),
        pytest.param(DEFAULT_CAPACITY*(2**4)-1, id="one-from-full list of default_capacity*(2^4)-1"),
        pytest.param(DEFAULT_CAPACITY*(2**6)-1, id="one-from-full list of default_capacity*(2^6)-1"),
        pytest.param(DEFAULT_CAPACITY*(2**8)-1, id="one-from-full list of default_capacity*(2^8)-1"),
        pytest.param(DEFAULT_CAPACITY*(2**10)-1, id="one-from-full list of default_capacity*(2^10)-1"),
        pytest.param(DEFAULT_CAPACITY*(2**0), id="full list of default_capacity*(2^0)"),
        pytest.param(DEFAULT_CAPACITY*(2**2), id="full list of default_capacity*(2^2)"),
        pytest.param(DEFAULT_CAPACITY*(2**4), id="full list of default_capacity*(2^4)"),
        pytest.param(DEFAULT_CAPACITY*(2**6), id="full list of default_capacity*(2^6)"),
        pytest.param(DEFAULT_CAPACITY*(2**8), id="full list of default_capacity*(2^8)"),
        pytest.param(DEFAULT_CAPACITY*(2**10), id="full list of default_capacity*(2^10)"),
        pytest.param(DEFAULT_CAPACITY*(2**10), id="full list of default_capacity*(2^10) ints"),
        pytest.param(DEFAULT_CAPACITY*(2**0) + 1, id="one-past-full list of default_capacity*(2^0)+1 ints"),
        pytest.param(DEFAULT_CAPACITY*(2**2) + 1, id="one-past-full list of default_capacity*(2^2)+1 ints"),
        pytest.param(DEFAULT_CAPACITY*(2**4) + 1, id="one-past-full list of default_capacity*(2^4)+1 ints"),
        pytest.param(DEFAULT_CAPACITY*(2**6) + 1, id="one-past-full list of default_capacity*(2^6)+1 ints"),
        pytest.param(DEFAULT_CAPACITY*(2**8) + 1, id="one-past-full list of default_capacity*(2^8)+1 ints"),
        pytest.param(DEFAULT_CAPACITY*(2**10) + 1, id="one-past-full list of default_capacity*(2^10)+1 ints"),
    ])
    
    def test_append_value_to_ArrayList(self, num_of_ints: int) -> None:
        """Tests if a user can append a default value to 
        the end of an ArrayList of a user-specified number of 
        random ints, without error.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        arraylist = rand_arraylist(num_of_ints)
        
        arraylist.append(DEFAULT_INT)
        
        assert TEST_RAN_WITHOUT_ERROR
        
        
class TestRemovingValueWithoutError:
    class TestRemovingStartValueWithoutError:
        @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id="list of one int"),
            pytest.param(2, id="list of two ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0)-1, id="one-from-full list of default_capacity*(2^0)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2)-1, id="one-from-full list of default_capacity*(2^2)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4)-1, id="one-from-full list of default_capacity*(2^4)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6)-1, id="one-from-full list of default_capacity*(2^6)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8)-1, id="one-from-full list of default_capacity*(2^8)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10)-1, id="one-from-full list of default_capacity*(2^10)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0), id="full list of default_capacity*(2^0) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2), id="full list of default_capacity*(2^2) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4), id="full list of default_capacity*(2^4) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6), id="full list of default_capacity*(2^6) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8), id="full list of default_capacity*(2^8) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10), id="full list of default_capacity*(2^10) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0) + 1, id="one-past-full list of default_capacity*(2^0)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2) + 1, id="one-past-full list of default_capacity*(2^2)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4) + 1, id="one-past-full list of default_capacity*(2^4)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6) + 1, id="one-past-full list of default_capacity*(2^6)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8) + 1, id="one-past-full list of default_capacity*(2^8)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10) + 1, id="one-past-full list of default_capacity*(2^10)+1 ints"),
        ])
        
        def test_remove_start_value_from_ArrayList(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the
            start index in an ArrayList of a user-specified 
            number of random ints, without error.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            arraylist = rand_arraylist(num_of_ints)
            
            arraylist.remove(0)
            
            assert TEST_RAN_WITHOUT_ERROR
            
    
    class TestRemovingMiddleValueWithoutError:
        @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id="list of one int"),
            pytest.param(2, id="list of two ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0)-1, id="one-from-full list of default_capacity*(2^0)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2)-1, id="one-from-full list of default_capacity*(2^2)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4)-1, id="one-from-full list of default_capacity*(2^4)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6)-1, id="one-from-full list of default_capacity*(2^6)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8)-1, id="one-from-full list of default_capacity*(2^8)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10)-1, id="one-from-full list of default_capacity*(2^10)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0), id="full list of default_capacity*(2^0) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2), id="full list of default_capacity*(2^2) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4), id="full list of default_capacity*(2^4) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6), id="full list of default_capacity*(2^6) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8), id="full list of default_capacity*(2^8) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10), id="full list of default_capacity*(2^10) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0) + 1, id="one-past-full list of default_capacity*(2^0)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2) + 1, id="one-past-full list of default_capacity*(2^2)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4) + 1, id="one-past-full list of default_capacity*(2^4)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6) + 1, id="one-past-full list of default_capacity*(2^6)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8) + 1, id="one-past-full list of default_capacity*(2^8)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10) + 1, id="one-past-full list of default_capacity*(2^10)+1 ints"),
        ])
        
        def test_remove_middle_value_from_ArrayList(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the 
            middle index of an ArrayList of a user-specified 
            number of random ints, without error.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            arraylist = rand_arraylist(num_of_ints)
            
            arraylist.remove(num_of_ints//2)
            
            assert TEST_RAN_WITHOUT_ERROR
            
            
    class TestRemovingLastValueWithoutError:
        @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id="list of one int"),
            pytest.param(2, id="list of two ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0)-1, id="one-from-full list of default_capacity*(2^0)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2)-1, id="one-from-full list of default_capacity*(2^2)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4)-1, id="one-from-full list of default_capacity*(2^4)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6)-1, id="one-from-full list of default_capacity*(2^6)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8)-1, id="one-from-full list of default_capacity*(2^8)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10)-1, id="one-from-full list of default_capacity*(2^10)-1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0), id="full list of default_capacity*(2^0) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2), id="full list of default_capacity*(2^2) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4), id="full list of default_capacity*(2^4) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6), id="full list of default_capacity*(2^6) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8), id="full list of default_capacity*(2^8) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10), id="full list of default_capacity*(2^10) ints"),
            pytest.param(DEFAULT_CAPACITY*(2**0) + 1, id="one-past-full list of default_capacity*(2^0)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**2) + 1, id="one-past-full list of default_capacity*(2^2)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**4) + 1, id="one-past-full list of default_capacity*(2^4)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**6) + 1, id="one-past-full list of default_capacity*(2^6)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**8) + 1, id="one-past-full list of default_capacity*(2^8)+1 ints"),
            pytest.param(DEFAULT_CAPACITY*(2**10) + 1, id="one-past-full list of default_capacity*(2^10)+1 ints"),
        ])
        
        def test_remove_last_value_from_ArrayList(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the 
            last index of an ArrayList of a user-specified 
            number of random ints, without error.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            arraylist = rand_arraylist(num_of_ints)
            
            arraylist.remove(num_of_ints-1)
            
            assert TEST_RAN_WITHOUT_ERROR