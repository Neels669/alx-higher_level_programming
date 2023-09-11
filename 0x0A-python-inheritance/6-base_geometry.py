#!/usr/bin/python3
"""This module defines a class BaseGeometry"""


class BaseGeometry:
    """based on 5-base_geometry.py"""

    def area(self):
        """raise exception is area is not implemented"""
        raise Exception("area() is not implemented")
