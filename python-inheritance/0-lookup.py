#!/usr/bin/python3
""" module: method for listing attributes and methods of objects"""


def lookup(obj):
    """ returns a list of available attributes and methods of an object

        args:
            obj

        return:
            list of attributes and methods
    """
    return dir(obj)
