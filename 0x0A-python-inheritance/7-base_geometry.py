#!/usr/bin/python3
"""This module defines a class BaseGeometry"""


class BaseGeometry:
    """based on 6-base_geometry.py"""

    def area(self):
        """raise exception is area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
