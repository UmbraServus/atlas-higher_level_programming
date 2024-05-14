#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Represents rectangle class"""


    def __init__(self, width=0, height=0):
        """initializes a new rectangle

            Args:
                width (int): Width of new rectangle
                height (int): Height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets/sets the width of reactangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets/sets height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must but >= 0")
        self.__height = value

        """modules"""

    def area(self):
        """returns area of rectangle width x height"""
        return self.__width * self.__height
    
    def perimeter(self):
        """return perimeter of rectangel w*2 + h*2"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
