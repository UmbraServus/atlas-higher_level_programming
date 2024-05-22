#!/usr/bin/python3
""" BaseGeometry class and methods """


class BaseGeometry():
    """ basegeometry class """

    def area(self):
        """ not implemented yet """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if value is an int or not

            args:
                self: itself
                name (str): name of itself
                value (int): value of itself

            raises:
                TypeError: if value is not an integer
                ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
