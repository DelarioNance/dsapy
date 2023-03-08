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
            pytest.param(1000, id='one-thousand ints'),
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
            pytest.param(1000, id='one-thousand ints'),
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
        
        arraylist.selection_sort(reverse=False)
        
        assert arraylist == sorted(pytest, reverse=False)
        
        
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
            pytest.param(1000, id='one-thousand ints'),
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
            pytest.param(1000, id='one-thousand ints'),
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
        
        arraylist.bubblesort(reverse=False)
        
        assert arraylist == sorted(pytest, reverse=False)
        
        
class TestInsertionSorting:
    """Uses GettingValue, GettingSize, and CheckingIfEqual modules.
    
    Unlike the end-to-end test methods for merge_sort and 
    quicksort, the insertion_sort test methods on ArrayLists with
    ten-thousand ints are ommited because insertion_sort runs 
    for a long time on large ArrayLists due to insertion_sort's
    worst-case running time of O(n^2).
    """
    def test_insertion_sort_ArrayList_of_one_int_in_ascending_order(self):
        pylist_of_one_int = rand_pylist(1)
        arraylist_of_one_int = ArrayList(pylist_of_one_int)
        
        pylist_of_one_int.sort()
        arraylist_of_one_int.insertion_sort()
        
        assert arraylist_of_one_int == pylist_of_one_int
        
    def test_insertion_sort_ArrayList_of_ten_ints_in_ascending_order(self):
        pylist_of_ten_ints = rand_pylist(10)
        arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
        
        pylist_of_ten_ints.sort()
        arraylist_of_ten_ints.insertion_sort()
        
        assert arraylist_of_ten_ints == pylist_of_ten_ints
        
    def test_insertion_sort_ArrayList_of_one_hundred_ints_in_ascending_order(self):
        pylist_of_one_hundred_ints = rand_pylist(100)
        arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
        pylist_of_one_hundred_ints.sort()
        arraylist_of_one_hundred_ints.insertion_sort()
        
        assert arraylist_of_one_hundred_ints == pylist_of_one_hundred_ints
        
    def test_insertion_sort_ArrayList_of_one_int_in_descending_order(self):
        pylist_of_one_int = rand_pylist(1)
        arraylist_of_one_int = ArrayList(pylist_of_one_int)
        
        pylist_of_one_int.sort(reverse=True)
        arraylist_of_one_int.insertion_sort(True)
        
        assert arraylist_of_one_int == pylist_of_one_int
        
    def test_insertion_sort_ArrayList_of_ten_ints_in_descending_order(self):
        pylist_of_ten_ints = rand_pylist(10)
        arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
        
        pylist_of_ten_ints.sort(reverse=True)
        arraylist_of_ten_ints.insertion_sort(True)
        
        assert arraylist_of_ten_ints == pylist_of_ten_ints
        
    def test_insertion_sort_ArrayList_of_one_hundred_ints_in_descending_order(self):
        pylist_of_one_hundred_ints = rand_pylist(100)
        arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
        pylist_of_one_hundred_ints.sort(reverse=True)
        arraylist_of_one_hundred_ints.insertion_sort(True)
        
        assert arraylist_of_one_hundred_ints == pylist_of_one_hundred_ints
        
class TestMergeSorting:
    """Uses GettingValue, GettingSize, and CheckingIfEqual modules.
    
    Unlike the end-to-end test methods for selection_sort,
    bubblesort, and insertion_sort, the mergesort test methods
    on ArrayLists with ten-thousand ints are included because
    mergesort does not run for a long time on large ArrayLists
    due to mergesort's worst-case running time of O(n log n).
    """
    def test_mergesort_ArrayList_of_one_int_in_ascending_order(self):
        pylist_of_one_int = rand_pylist(1)
        arraylist_of_one_int = ArrayList(pylist_of_one_int)
        
        pylist_of_one_int.sort()
        sorted_arraylist_of_one_int = arraylist_of_one_int.mergesort()
        
        assert sorted_arraylist_of_one_int == pylist_of_one_int
        
    def test_mergesort_ArrayList_of_ten_ints_in_ascending_order(self):
        pylist_of_ten_ints = rand_pylist(10)
        arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
        
        pylist_of_ten_ints.sort()
        sorted_arraylist_of_ten_ints = arraylist_of_ten_ints.mergesort()
        assert sorted_arraylist_of_ten_ints == pylist_of_ten_ints
        
    def test_mergesort_ArrayList_of_one_hundred_ints_in_ascending_order(self):
        pylist_of_one_hundred_ints = rand_pylist(100)
        arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
        pylist_of_one_hundred_ints.sort()
        sorted_arraylist_of_one_hundred_ints = arraylist_of_one_hundred_ints.mergesort()
        
        assert sorted_arraylist_of_one_hundred_ints == pylist_of_one_hundred_ints
        
    def test_mergesort_ArrayList_of_ten_thousand_ints_in_ascending_order(self):
        pylist_of_ten_thousand_ints = rand_pylist(10000)
        arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
        pylist_of_ten_thousand_ints.sort()
        sorted_arraylist_of_ten_thousand_ints = arraylist_of_ten_thousand_ints.mergesort()
        
        assert sorted_arraylist_of_ten_thousand_ints == pylist_of_ten_thousand_ints
        
    def test_mergesort_ArrayList_of_one_int_in_descending_order(self):
        pylist_of_one_int = rand_pylist(1)
        arraylist_of_one_int = ArrayList(pylist_of_one_int)
        
        pylist_of_one_int.sort(reverse=True)
        sorted_arraylist_of_one_int = arraylist_of_one_int.mergesort(True)
        
        assert sorted_arraylist_of_one_int == pylist_of_one_int
        
    def test_mergesort_ArrayList_of_ten_ints_in_descending_order(self):
        pylist_of_ten_ints = rand_pylist(10)
        arraylist_of_ten_ints = ArrayList(pylist_of_ten_ints)
        
        pylist_of_ten_ints.sort(reverse=True)
        sorted_arraylist_of_ten_ints = arraylist_of_ten_ints.mergesort(True)
        
        assert sorted_arraylist_of_ten_ints == pylist_of_ten_ints
        
    def test_mergesort_ArrayList_of_one_hundred_ints_in_descending_order(self):
        pylist_of_one_hundred_ints = rand_pylist(100)
        arraylist_of_one_hundred_ints = ArrayList(pylist_of_one_hundred_ints)
        
        pylist_of_one_hundred_ints.sort(reverse=True)
        sorted_arraylist_of_one_hundred_ints = arraylist_of_one_hundred_ints.mergesort(True)
        
        assert sorted_arraylist_of_one_hundred_ints == pylist_of_one_hundred_ints
        
    def test_mergesort_ArrayList_of_ten_thousand_ints_in_descending_order(self):
        pylist_of_ten_thousand_ints = rand_pylist(10000)
        arraylist_of_ten_thousand_ints = ArrayList(pylist_of_ten_thousand_ints)
        
        pylist_of_ten_thousand_ints.sort(reverse=True)
        sorted_arraylist_of_ten_thousand_ints = arraylist_of_ten_thousand_ints.mergesort()
        
        assert sorted_arraylist_of_ten_thousand_ints == pylist_of_ten_thousand_ints