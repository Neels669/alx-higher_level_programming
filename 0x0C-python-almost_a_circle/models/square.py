#!/usr/bin/python3
"""This module defines a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a Sqaure inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the string representation of an object """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the attributes of square """
        if args != ():
            if len(args) >= 2:
                newargs = args[0:2] + args[1:]
            else:
                newargs = args
            super().update(*newargs)
        else:
            newkwargs = dict()
            for k, v in kwargs.items():
                if k == "size":
                    newkwargs["width"] = v
                    newkwargs["height"] = v
                else:
                    newkwargs[k] = v
            super().update(**newkwargs)
