#!/usr/bin/python3
"""This module defines a sqaure based on 4-square.py"""


class Sqaure:
    """This class represents a square attributed to size"""

    def __init__(self, size=0):
        """ initialize square objects,
        sets size equal to 0 by default,
        checks if size has the correct type and value """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Initialization of variable"""
        return self.__size

    @size.setter
    def size(self, value):
        """Inizialitation of variables"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Initialize the variable"""
        return self.__size ** 2

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
