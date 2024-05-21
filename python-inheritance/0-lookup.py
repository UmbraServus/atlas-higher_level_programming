#!/usr/bin/python3

def lookup(obj):
    """ returns a list of available attributes and methods of an object

        args:
            obj

        return:
            list of attributes and methods
    """
    return dir(obj)
