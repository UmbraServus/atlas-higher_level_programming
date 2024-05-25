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
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self._validator_method(width, "width")
        self._validator_method(height, "height")
        self._validator_method(x, "x")
        self._validator_method(y, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        """ methods/setters/getters """

    def _validator_method(self, value, name):
        """ validates all the setters and instantiations

            args:
                value (int): variable to be validated
                name (str): name of the attribute to be validated
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"]:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"]:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    def area(self):
        """ returns the area of a rectangle height * width"""
        return self.__width * self.__height

    def display(self):
        """ prints to stdout a representation of a rectangle using "#" """
        for row in range(self.__height):
            for column in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

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
        self._validator_method(new_width, "width")
        self.__width = new_width

    @height.setter
    def height(self, new_height):
        self._validator_method(new_height, "height")
        self.__height = new_height

    @x.setter
    def x(self, new_x):
        self._validator_method(new_x, "x")
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        self._validator_method(new_y, "y")
        self.__y = new_y
