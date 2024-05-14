#!/usr/bin/python3
""" Integer addition function"""

def add_integer(a, b=98):
    """Returns addition of a and b
    
    Float args are casted into ints before addition
    
    Raises:
        TypeError: If a or b is either a non-int or non-float
    """
    if((not isinstance(a, int))) and ((not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif ((not isinstance(b, int))) and ((not isinstance(b, float))):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))