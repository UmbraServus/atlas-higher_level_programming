#!/usr/bin/python3
""" module for square class """


class Square:
    """ square class """
    def __init__(self, size=0):
        """initialze square
        Args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """returns size of the square instance
            setter sets the size of the square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of a square"""
        return self.__size * self.__size
    
    def my_print(self):
        """ prints out a square the size of the instance of square class"""
        if self.__size == 0:
            print("")
        else:
            for rows in range(self.__size):
                print("#" * self.__size)
