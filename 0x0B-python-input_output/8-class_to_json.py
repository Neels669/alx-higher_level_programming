#!/usr/bin/python3
"""This module defines function class_to_json"""


def class_to_json(obj):
    """dictionary description of simple data structure
    for JSON serialization
    """
    return obj.__dict__
