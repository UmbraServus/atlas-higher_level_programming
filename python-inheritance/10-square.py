#!/usr/bin/python3
"""Module documentation"""


Rectangle = __import__("9-rectangle.py").Rectangle

class Square(Rectangle):
    """ inherit Rectangle and basegeometry methods and attributes """


    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
