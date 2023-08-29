#!/usr/bin/python3
"This module defines a Square based on 4-square.py"


class Square:
    """This defines a class Sqare"""

    def __init__(self, size=0):
        """Inizialitation of variables
        Arg self identificador
        size of square
        """
        self.size = size

    @property
    def size(self):
        """Inizialitation of variables
        Arg self identificador
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Inizialitation of variables
        Arg self identificador
        value of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise valueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area os the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
