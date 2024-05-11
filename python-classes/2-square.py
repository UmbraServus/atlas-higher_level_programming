#!/usr/bin/python3
""" module for square class """


class Square:
    """ square class with private size attribute """
    def __init__(self, size=0):
        """initialze square
        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size