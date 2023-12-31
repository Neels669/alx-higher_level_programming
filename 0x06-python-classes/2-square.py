#!/usr/bin/python3
"""This module defines a Sqaure based on 1-square.py"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0):
        """initialize square objects,
        sets size equal to 0 by default,
        checks if size has the correct type and value """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
