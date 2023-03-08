"""
A Python script for end-to-end testing the ArrayList class 
with PyTest.

Author: Delario Nance, Jr.
Date: February 15, 2023 - March 7, 2023
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
DEFAULT_ZERO_INT_IN_ARRAYLIST = 0
DEFAULT_POSITIVE_INT_IN_ARRAYLIST = 1
DEFAULT_POSITIVE_INT_NOT_IN_ARRAYLIST = 1729
DEFAULT_NEGATIVE_INT_IN_ARRAYLIST = -1
DEFAULT_NEGATIVE_INT_NOT_IN_ARRAYLIST = -1729


class TestGettingMinimum:
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            pytest.param(1000, id='one-thousand ints'),
            pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_get_min_in_ArrayList(self, num_of_ints: int) -> None:
        """Tests if a user can get the minimum value on an
        ArrayList of a user-specified number of random ints.

        Args:
            num_of_ints (int): The user-specified number of 
                random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        min_of_arraylist = arraylist.min()
        
        assert min_of_arraylist == min(pylist)
        
        
class TestGettingMaximum:
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            pytest.param(1000, id='one-thousand ints'),
            pytest.param(10000, id='ten-thousand ints')
    ])
        
    def test_get_max_in_ArrayList(self, num_of_ints: int) -> None:
        """Tests if a user can get the maximum value on an
        ArrayList of a user-specified number of random ints.

        Args:
            num_of_ints (int): The user-specified number of 
                random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        min_of_arraylist = arraylist.max()
        
        assert min_of_arraylist == max(pylist)
        
        
class TestReversing:
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            pytest.param(1000, id='one-thousand ints'),
            pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_reverse_ArrayList(self, num_of_ints: int) -> None:
        """Tests if a user can reverse the values in an 
        ArrayList of a user-specified number of random ints.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        arraylist = rand_arraylist(num_of_ints)
        copy_of_arraylist = arraylist.copy()
        
        arraylist.reverse()
        arraylist.reverse()
        
        assert arraylist == copy_of_arraylist
        
        
class TestSelectionSorting:
    """Unlike the end-to-end test methods for merge_sort and 
    quicksort, the selection_sort test methods on ArrayLists 
    with ten-thousand ints are ommited because selection_sort 
    runs for a long time on large ArrayLists due to 
    selection_sort's worst-case running time of O(n^2).
    """
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            # pytest.param(1000, id='one-thousand ints'), SLOW
            # pytest.param(10000, id='ten-thousand ints') SLOW
    ])
    
    def test_selection_sort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pytest = rand_pylist(num_of_ints)
        arraylist = ArrayList(pytest)
        
        arraylist.selection_sort(reverse=False)
        
        assert arraylist == sorted(pytest, reverse=False)
    
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            # pytest.param(1000, id='one-thousand ints'), SLOW
            # pytest.param(10000, id='ten-thousand ints') SLOW
    ])
    
    def test_selection_sort_ArrayList_in_descending_order(self, num_of_ints) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pytest = rand_pylist(num_of_ints)
        arraylist = ArrayList(pytest)
        
        arraylist.selection_sort(reverse=True)
        
        assert arraylist == sorted(pytest, reverse=True)
        
        
class TestBubbleSorting:
    """Unlike the end-to-end test methods for merge_sort and 
    quicksort, the bubblesort test methods on ArrayLists 
    with ten-thousand ints are ommited because bubblesort 
    runs for a long time on large ArrayLists due to 
    bubblesort's worst-case running time of O(n^2).
    """
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            # pytest.param(1000, id='one-thousand ints'), SLOW
            # pytest.param(10000, id='ten-thousand ints') SLOW
    ])
    
    def test_bubblesort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pytest = rand_pylist(num_of_ints)
        arraylist = ArrayList(pytest)
        
        arraylist.bubblesort(reverse=False)
        
        assert arraylist == sorted(pytest, reverse=False)
    
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            # pytest.param(1000, id='one-thousand ints'), SLOW
            # pytest.param(10000, id='ten-thousand ints') SLOW
    ])
    
    def test_bubblesort_ArrayList_in_descending_order(self, num_of_ints) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pytest = rand_pylist(num_of_ints)
        arraylist = ArrayList(pytest)
        
        arraylist.bubblesort(reverse=True)
        
        assert arraylist == sorted(pytest, reverse=True)
        
        
class TestInsertionSorting:
    """Unlike the end-to-end test methods for merge_sort and 
    quicksort, the insertion_sort test methods on ArrayLists 
    with ten-thousand ints are ommited because insertion_sort 
    runs for a long time on large ArrayLists due to 
    insertion_sort's worst-case running time of O(n^2).
    """
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            # pytest.param(1000, id='one-thousand ints'), SLOW
            # pytest.param(10000, id='ten-thousand ints') SLOW
    ])
    
    def test_insertion_sort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pytest = rand_pylist(num_of_ints)
        arraylist = ArrayList(pytest)
        
        arraylist.insertion_sort(reverse=False)
        
        assert arraylist == sorted(pytest, reverse=False)
    
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            # pytest.param(1000, id='one-thousand ints'), SLOW
            # pytest.param(10000, id='ten-thousand ints') SLOW
    ])
    
    def test_insertion_sort_ArrayList_in_descending_order(self, num_of_ints) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pytest = rand_pylist(num_of_ints)
        arraylist = ArrayList(pytest)
        
        arraylist.insertion_sort(reverse=True)
        
        assert arraylist == sorted(pytest, reverse=True)
        
        
class TestMergeSorting:
    """Unlike the end-to-end test methods for selection_sort,
    bubblesort, and insertion_sort, the mergesort test methods
    on ArrayLists with ten-thousand ints are included because
    mergesort does not run for a long time on large ArrayLists
    due to mergesort's worst-case running time of O(n log n).
    """
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            pytest.param(1000, id='one-thousand ints'),
            pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_mergesort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pytest = rand_pylist(num_of_ints)
        arraylist = ArrayList(pytest)
        
        sorted_arraylist = arraylist.mergesort(reverse=False)
        
        assert sorted_arraylist == sorted(pytest, reverse=False)
    
    @pytest.mark.parametrize("num_of_ints", [
            pytest.param(1, id='one int'),
            pytest.param(10, id='ten ints'),
            pytest.param(100, id='one-hundred ints'),
            pytest.param(1000, id='one-thousand ints'),
            pytest.param(10000, id='ten-thousand ints'),
    ])
    
    def test_mergesort_ArrayList_in_descending_order(self, num_of_ints) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pytest = rand_pylist(num_of_ints)
        arraylist = ArrayList(pytest)
        
        sorted_arraylist = arraylist.mergesort(reverse=True)
        
        assert sorted_arraylist == sorted(pytest, reverse=True)