"""
A Python script for integration testing the ArrayList class 
with PyTest.

Author: Delario Nance, Jr.
"""

# Standard library imports
import random # for selecting random ints
from pathlib import Path # for retrieving filepaths
import sys # for adding filepaths

# Accessing project directories
FILEPATH_TO_TESTING = str(Path(__file__) # path to this file
                          .parent # path to folder of unit tests
                          .parent # path to folder of tests
                          )
FILEPATH_TO_SRC = str(Path(__file__)
                      .parent # path to folder of unit tests
                      .parent # path to folder of tests
                      .parent # path to project folder
                      / "src" # path to folder of data structures
                      )
sys.path.append(FILEPATH_TO_TESTING)
sys.path.append(FILEPATH_TO_SRC)

# Related third part imports
import pytest # for markers

# Local application imports
from ArrayList import ArrayList
from helpers import *

# Global variables
DEFAULT_CAPACITY = 16
DEFAULT_INT = 1729
DUMMY_NEGATIVE_INT = -2 # Not -1 because -1 is the dummy negative int for ArrayLists
INDEX_BEFORE_NEWLINE = -1
TEST_RAN_WITHOUT_ERROR = True


class TestSettingValueWithCorrectNewValue:
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
    
    def test_set_value_in_ArrayList_with_correct_new_value(self, num_of_ints: int, index: int) -> None:
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


class TestAppendingValueWithCorrectNewSize:
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
    
    def test_append_value_to_ArrayList_with_correct_new_size(self, num_of_ints: int) -> None:
        """Tests if a user can append a default value to 
        the end of an ArrayList of a user-specified number of 
        random ints, with the correct new size.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        arraylist = rand_arraylist(num_of_ints)
        
        arraylist.append(DEFAULT_INT)
        
        assert len(arraylist) == num_of_ints + 1
   
        
class TestAppendingValueWithCorrectNewValue:
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
    
    def test_append_value_to_ArrayList_with_correct_new_value(self, num_of_ints: int) -> None:
        """Tests if a user can append a default value to 
        the end of an ArrayList of a user-specified number of 
        random ints, with the correct new value.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        arraylist = rand_arraylist(num_of_ints)
        
        arraylist.append(DEFAULT_INT)
        
        assert arraylist[num_of_ints] == DEFAULT_INT
        
        
class TestRemovingValueWithCorrectNewSize:
    class TestRemovingStartValueWithCorrectNewSize:
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
        
        def test_remove_start_value_from_ArrayList_with_correct_new_size(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the
            start index in an ArrayList of a user-specified 
            number of random ints, with the correct new size.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            arraylist = rand_arraylist(num_of_ints)
            
            arraylist.remove(0)
            
            assert len(arraylist) == num_of_ints - 1
            
    
    class TestRemovingMiddleValueWithCorrectNewSize:
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
        
        def test_remove_middle_value_from_ArrayList_with_correct_new_size(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the 
            middle index of an ArrayList of a user-specified 
            number of random ints, with the correct new size.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            arraylist = rand_arraylist(num_of_ints)
            
            arraylist.remove(num_of_ints//2)
            
            assert len(arraylist) == num_of_ints - 1
            
            
    class TestRemovingLastValueWithCorrectNewSize:
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
        
        def test_remove_last_value_from_ArrayList_with_correct_new_size(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the 
            last index of an ArrayList of a user-specified 
            number of random ints, with the correct new size.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            arraylist = rand_arraylist(num_of_ints)
            
            arraylist.remove(num_of_ints-1)
            
            assert len(arraylist) == num_of_ints - 1
    
            
class TestCheckingForEquality:
    """In the TestCheckingIfEqualForSameSizeButDifferentValues 
    class for ensuring that ArrayLists of the same size but 
    with different values are considered unequal, my choice of
    using random values for our ArrayLists could
    theoretically produce ArrayLists with the same values
    (hence equal ArrayLists). However, since we are using 
    random integers in the range [-1000,1000], the 
    probability of since an event happening is equal to the
    fraction 1/(2001^n), where n is the size of both 
    ArrayLists. This fraction takes on a very low maximum 
    value of 0.05% (when n=1), so we will use random integers
    in the TestCheckingIfEqualForSameSizeButDifferentValues 
    class.
    """
    class TestCheckingIfEqualForSameSizeAndSameValues:
        @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(5, id='five ints'),
            pytest.param(10, id='ten ints'),
            pytest.param(55, id='fifty-five ints'),
            pytest.param(100, id='one-hundred ints'),
            pytest.param(555, id='five hundred fifty-five ints'),
            pytest.param(1000, id='one-thousand ints'),
            pytest.param(5555, id='five thousand five hundred fifty-five ints'),
            pytest.param(10000, id='ten-thousand ints')
        ])
        
        def test_check_if_ArrayLists_of_same_size_and_same_values_are_equal(self, num_of_ints: int) -> None:
            """Tests if a user can determine if two ArrayLists
            of the same user-specified size and same random 
            ints are truly equal.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            pylist = rand_pylist(num_of_ints)
            first_arraylist = ArrayList(pylist)
            second_arraylist = ArrayList(pylist)
            
            verdict = (first_arraylist == second_arraylist)
            
            assert verdict == True
              
    
    class TestCheckingIfUnequalForSameSizeAndDifferentValues:
        @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            pytest.param(1000, id='one-thousand ints'),
            pytest.param(10000, id='ten-thousand ints')
        ])
        
        def test_check_if_ArrayLists_of_same_size_and_different_values_are_unequal(self, num_of_ints: int) -> None:
            """Tests if a user can determine if two ArrayLists
            of the same user-specified size but different 
            random ints are truly unequal.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            first_arraylist =  rand_arraylist(num_of_ints)
            second_arraylist = rand_arraylist(num_of_ints)
            
            verdict = (first_arraylist != second_arraylist)
            
            assert verdict == True
        
    
    class TestCheckingIfEqualForDifferentSizes:
        @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            pytest.param(1000, id='one-thousand ints'),
            pytest.param(10000, id='ten-thousand ints')
        ])
        
        def test_check_if_ArrayLists_of_different_sizes_are_unequal(self, num_of_ints: int) -> None:
            """Tests if a user can determine if an ArrayList
            of a user-specified size and an ArrayList with
            a different (default test int) size are truly 
            unequal.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            first_arraylist = rand_arraylist(num_of_ints)
            second_arraylist = rand_arraylist(DEFAULT_INT)
            
            verdict = (first_arraylist != second_arraylist)
            
            assert verdict == True

            
class TestRemovingValueWithCorrectOldValues:
    class TestRemovingStartValueWithCorrectOldValues:
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
        
        def test_remove_start_value_from_ArrayList_with_correct_old_values(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the
            start index in an ArrayList of a user-specified 
            number of random ints, with the correct old values.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            pylist = rand_pylist(num_of_ints)
            arraylist = ArrayList(pylist)
            
            pylist.pop(0)
            arraylist.remove(0)
            
            assert pylist == arraylist
            
    
    class TestRemovingMiddleValueWithCorrectOldValues:
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
        
        def test_remove_middle_value_from_ArrayList_with_correct_old_values(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the 
            middle index of an ArrayList of a user-specified 
            number of random ints, with the correct old values.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            pylist = rand_pylist(num_of_ints)
            arraylist = ArrayList(pylist)
            
            pylist.pop(num_of_ints//2)
            arraylist.remove(num_of_ints//2)
            
            assert pylist == arraylist
            
            
    class TestRemovingLastValueWithCorrectOldValues:
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
        
        def test_remove_last_value_from_ArrayList_with_correct_old_values(self, num_of_ints: int) -> None:
            """Tests if a user can remove the value at the 
            last index of an ArrayList of a user-specified 
            number of random ints, with the correct old values.

            Args:
                num_of_ints (int): The user-specified number of 
                random ints
            """
            pylist = rand_pylist(num_of_ints)
            arraylist = ArrayList(pylist)
            
            pylist.pop(-1)
            arraylist.remove(-1)
            
            assert pylist == arraylist