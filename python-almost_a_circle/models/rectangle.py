#!/usr/bin/python3
""" Module: class Rectangle(Base)"""

from models.base import Base

class Rectangle(Base):
    """ Rectangle class:

        Attributes:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): position in rectangle
            y (int): position in rectangle
    """
    def __init__(self, width, height, x = 0, y = 0, id = None):
        super().__init__(id):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, new_width):
        self.__width = new_width
    
    @height.setter
    def height(self, new_height):
        self.__height = new_height
    
    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        self.__y = new_y
