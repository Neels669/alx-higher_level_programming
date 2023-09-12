#!/usr/bin/python3
"""This module defines a function to_json_string"""


import json


def to_json_string(my_obj):
    """ json representation of object"""
    return json.dumps(my_obj)
