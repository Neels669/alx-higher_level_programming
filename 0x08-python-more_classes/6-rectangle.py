#!/usr/bin/python3
"""This module defines a rectangle class"""


class Rectangle:
    """This class defines a rectangle based on 2-rectangle.py"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ instantiation """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ returns a printable string when print is called """
        ch = ""
        if self.__width == 0 or self.__height == 0:
            return ch
        for i in range(self.__height):
            for j in range(self.__width):
                ch += "#"
            ch += '\n'
        return ch[:-1]

    def __repr__(self):
        """ returns a string that creates a new object when evaluated """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ called when an object is deleted with del """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
