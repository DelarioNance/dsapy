"""
A Python program containing the definitions of various helper 
functions used in the unit, integration, and end-to-end test
scripts.

Author: Delario Nance, Jr.
Date: January 24, 2023 - January 24, 2023
"""

from src.ArrayList import ArrayList

def random_array_list(size: int) -> ArrayList:
    """Returns an ArrayList of a user-specified size, of random 
    integers in the range [-1000,1000].

    Args:
        size (int): The user-specified size

    Returns:
        ArrayList: The ArrayList of random integers
    """