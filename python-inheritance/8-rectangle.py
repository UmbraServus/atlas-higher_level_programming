#!/usr/bin/python3
"""module documentation """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class with inheritance from BaseGeometry

        Methods:
            Area(): Not implemented yet
            Integer_validator(): validates if given value is an integer
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
