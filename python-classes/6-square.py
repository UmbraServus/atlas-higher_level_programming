#!/usr/bin/python3
""" module for square class """


class Square:
    """ square class """
    def __init__(self, size=0, position=(0, 0)):
        """initialze square
        Args:
            size (int): size of the square.
            position (int, int): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """returns size of the square in stance
            setter sets the size of the square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns current position in square
            setter sets position in square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
            all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """ prints out a square the size of the instance of square class
            with position added"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
