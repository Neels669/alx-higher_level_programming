#!/usr/bin/python3
"""This module defines a funcion read_file"""


def read_file(filename=""):
    """ reads a text file and prints its content """
    with open(filename) as f:
        for line in f:
            print(line, end="")
