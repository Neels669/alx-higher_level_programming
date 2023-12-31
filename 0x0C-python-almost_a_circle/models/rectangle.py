#!/usr/bin/python3
"""This module defines a class class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ returns the area value of each rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle in stdout with '#' """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ string representation of the object """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        count = 0
        if args != ():
            for a in args:
                count += 1
                if count == 1:
                    self.id = a
                if count == 2:
                    self.width = a
                if count == 3:
                    self.height = a
                if count == 4:
                    self.x = a
                if count == 5:
                    self.y = a
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        newd = dict()
        newd["id"] = self.id
        newd["width"] = self.width
        newd["height"] = self.height
        newd["x"] = self.x
        newd["y"] = self.y
        return newd
