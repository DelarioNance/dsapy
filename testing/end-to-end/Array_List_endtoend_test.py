"""
A Python script for end-to-end testing the ArrayList class 
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
DEFAULT_ZERO_INT_IN_ARRAYLIST = 0
DEFAULT_POSITIVE_INT_IN_ARRAYLIST = 1
DEFAULT_POSITIVE_INT_NOT_IN_ARRAYLIST = 1729
DEFAULT_NEGATIVE_INT_IN_ARRAYLIST = -1
DEFAULT_NEGATIVE_INT_NOT_IN_ARRAYLIST = -1729


class TestGettingMinimum:
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(1, id='one int'),
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
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
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
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
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
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
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_selection_sort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order, using selection sort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        arraylist.selection_sort(reverse=False)
        
        assert arraylist == sorted(pylist, reverse=False)
    
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(1, id='one int'),
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_selection_sort_ArrayList_in_descending_order(self, num_of_ints) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order, using selection sort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        arraylist.selection_sort(reverse=True)
        
        assert arraylist == sorted(pylist, reverse=True)
        
        
class TestBubbleSorting:
    """Unlike the end-to-end test methods for merge_sort and 
    quicksort, the bubblesort test methods on ArrayLists 
    with ten-thousand ints are ommited because bubblesort 
    runs for a long time on large ArrayLists due to 
    bubblesort's worst-case running time of O(n^2).
    """
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(1, id='one int'),
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_bubblesort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order, using bubblesort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        arraylist.bubblesort(reverse=False)
        
        assert arraylist == sorted(pylist, reverse=False)
    
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(1, id='one int'),
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_bubblesort_ArrayList_in_descending_order(self, num_of_ints) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order, using bubblesort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        arraylist.bubblesort(reverse=True)
        
        assert arraylist == sorted(pylist, reverse=True)
        
        
class TestInsertionSorting:
    """Unlike the end-to-end test methods for merge_sort and 
    quicksort, the insertion_sort test methods on ArrayLists 
    with ten-thousand ints are ommited because insertion_sort 
    runs for a long time on large ArrayLists due to 
    insertion_sort's worst-case running time of O(n^2).
    """
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(1, id='one int'),
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_insertion_sort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order, using insertion sort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        arraylist.insertion_sort(reverse=False)
        
        assert arraylist == sorted(pylist, reverse=False)
    
    @pytest.mark.parametrize("num_of_ints", [
        pytest.param(1, id='one int'),
        pytest.param(5, id='five ints'),
        pytest.param(10, id='ten ints'),
        pytest.param(55, id='fifty-five ints'),
        pytest.param(100, id='one-hundred ints'),
        pytest.param(555, id='five hundred fifty-five ints'),
        # pytest.param(1000, id='one-thousand ints'),
        # pytest.param(5555, id='five thousand five hundred fifty-five ints'),
        # pytest.param(10000, id='ten-thousand ints')
    ])
    
    def test_insertion_sort_ArrayList_in_descending_order(self, num_of_ints) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order, using insertion sort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        arraylist.insertion_sort(reverse=True)
        
        assert arraylist == sorted(pylist, reverse=True)
        
        
class TestMergeSorting:
    """Unlike the end-to-end test methods for selection_sort,
    bubblesort, and insertion_sort, the mergesort test methods
    on ArrayLists with ten-thousand ints are included because
    mergesort does not run for a long time on large ArrayLists
    due to mergesort's worst-case running time of O(n log n).
    """
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
    
    def test_mergesort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order, using mergesort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        sorted_arraylist = arraylist.mergesort(reverse=False)
        
        assert sorted_arraylist == sorted(pylist, reverse=False)
    
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
    
    def test_mergesort_ArrayList_in_descending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order, using mergesort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        sorted_arraylist = arraylist.mergesort(reverse=True)
        
        assert sorted_arraylist == sorted(pylist, reverse=True)
        
        
class TestQuickSorting:
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
    
    def test_quicksort_ArrayList_in_ascending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in ascending
        order, using quicksort.
        
        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        arraylist = ArrayList(pylist)
        
        arraylist.quicksort(reverse=False)
        
        assert arraylist == sorted(pylist, reverse=False)
        
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
    
    def test_quicksort_ArrayList_in_descending_order(self, num_of_ints: int) -> None:
        """Tests if a user can sort the values in an ArrayList
        of a user-specified number of random ints, in descending
        order, using quicksort.

        Args:
            num_of_ints (int): The user-specified number of 
            random ints
        """
        pylist = rand_pylist(num_of_ints)
        print(pylist)
        arraylist = ArrayList(pylist)
        
        arraylist.quicksort(reverse=True)
        
        assert arraylist == sorted(pylist, reverse=True)