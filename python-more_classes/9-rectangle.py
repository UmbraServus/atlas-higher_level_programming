#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Represents rectangle class

    Attributes:
        number_of_instances (int): number of rectangle instances
        print_symbol (any): character to be used in str() or print()
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes a new rectangle

            Args:
                width (int): Width of new rectangle
                height (int): Height of the new rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("height must be >= 0")
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

    def __str__(self):
        """returns repesentation of square using print_symbol variable """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = ""
        for x in range(self.__height):
            rectangle += f"{self.print_symbol}" * self.__width
            if x < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """ returns official representation str of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints bye rectangle when del is detected"""
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """checks if rect 1 is bigger or equal to rect 2
            Args:
                rect_1: rectangle one
                rect_2: rectangle two
            Raise:
                TypeError: if rect1 or rect2 are not a Rectangle type
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
       return cls(size, size)
