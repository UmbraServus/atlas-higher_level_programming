#!/usr/bin/python3
""" checks to see if object is an instance of a class that inherited 
    from the given class """

def inherits_from(obj, a_class):
    """ checks if obj is an instance of class that inherited from given class

        args:
            obj: object to check against a_class to see if object inherited from class
            a_class: the class to be checked against

        return:
            true or false
    """
    return issubclass(obj, a_class)
