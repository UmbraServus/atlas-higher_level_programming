#!/usr/bin/python3
""" checks to see if the given object is an instance of or if object is an
    instance of a class that inherited from the given class. """


def is_kind_of_class(obj, a_class):
    """ determines if object is an instance of or if object is an instance of
        a class that inherited from the specified class

        args:
            obj: object to check
            a_class: the class to check against and see if instance is the same

        return:
            True or False
    """
    return isinstance(obj, a_class)
