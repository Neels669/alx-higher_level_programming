#!/usr/bin/python3
"""This moduule defines a function append_write"""


def append_write(filename="", text=""):
    """appened string at end"""

    with open(filename, mode="a") as data_file:
        return data_file.write(text)
