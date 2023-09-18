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
            if value <= 0:
                raise ValueError("Width must be greater than 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if value <= 0:
                raise ValueError("Height must be greater than 0")
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if value < 0:
                raise ValueError("X coordinate cannot be negative")
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if value < 0:
                raise ValueError("Y coordinate cannot be negative")
            self.__y = value