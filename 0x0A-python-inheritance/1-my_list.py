#!/usr/bin/python3
"""This mode defines a class MyList"""


class MyList(list):
    """Type class MyList  with print_sorted function"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
