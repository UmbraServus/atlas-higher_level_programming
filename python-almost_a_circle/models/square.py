#!/usr/bin/python3
""" Module: Square class that inherits from Rectangle """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class that inherits from rectangle 
        
        attributes: all the same except now height and width are both size
         due to a square being equal on all sides.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
