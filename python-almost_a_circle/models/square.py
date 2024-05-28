#!/usr/bin/python3
""" Module: Square class that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from rectangle

        attributes: all the same except now height and width are both size
         due to a square being equal on all sides.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """ methods/setters/getters """

    def __str__(self):
        """returns an overridden str rep of the self."""
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - "
            f"{self.size}"
        )

    def update(self, *args, **kwargs):
        """ updates each of the attributes based on a how many parameters
            are passed to args. """
        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns a dictionary representation of attributes"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, new_size):
        self._validator_method(new_size, "width")
        self.width = new_size
        self.height = new_size
