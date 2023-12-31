#!/usr/bin/python3
"""This module defines a sqaure based on 5-square.py"""


class Square:
    """This represents a class Sqaure"""

    def __init__(self, size=0, position=(0, 0)):
        """Inizialitation of variables
        Arg self identificador
        posicion of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Inizialitation of variables
        Arg self identificador
        posicion of square
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

    @property
    def position(self):
        """private tribute to get the postion of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """private tribute to get the postion of the square"""
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area os the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
