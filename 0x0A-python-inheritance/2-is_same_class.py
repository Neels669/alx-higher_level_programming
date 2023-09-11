#!/usr/bin/python3
"""This module defines function is_same_class."""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the specified class"""
    if type(obj) == a_class:
        return True
    else:
        return False
