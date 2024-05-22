#!/usr/bin/python3
""" checks to make sure object is an instance of specified class """


def is_same_class(obj, a_class):
    """ returns true or false based on wethere or not object is an instance of the given class

        args:
            obj: object to compare if it an instance of given class
            a_class: a class to see if object is an instance of the class

        return: true or false
    """
    return isinstance(obj, a_class)
