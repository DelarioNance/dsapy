"""
A Python script for unit testing the ArrayList class.

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 24, 2023
"""

import sys
sys.path.append("c:\\Users\\Delar\\OneDrive\\Desktop\\Winter Break\\Repos\\DSAPy\\dsapy\\src")
sys.path.append("c:\\Users\\Delar\\OneDrive\\Desktop\\Winter Break\\Repos\\DSAPy\\dsapy\\testing")

from ArrayList import ArrayList
from helpers import rand_array_list

class testGettingSize:
    def test_get_size_of_empty_ArrayList(self):

        empty_arraylist = ArrayList()
        size = len(empty_arraylist)
        assert size == 0