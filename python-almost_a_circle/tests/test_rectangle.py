#!/usr/bin/python3
""" Module: contains unittests for Base class """
import unittest
from models.rectangle import Rectangle


class TestRectangleclass(unittest.TestCase):
    """ Unittests for Rectangle """

    def test_rectangle_instance(self):
        rect1 = Rectangle(1, 2)
        self.assertIsInstance(rect1, Rectangle)

        rect2 = Rectangle(1, 2, 3)
        self.assertIsInstance(rect2, Rectangle)

        rect3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(rect3, Rectangle)

        with self.assertRaises(TypeError):
            Rectangle(7, "14")

        with self.assertRaises(TypeError):
            Rectangle("7", 14)

        with self.assertRaises(TypeError):
            Rectangle(7, 14, "1")

        with self.assertRaises(TypeError):
            Rectangle(7, 14, 1, "2")

        with self.assertRaises(ValueError):
            Rectangle(-7, 14)

        with self.assertRaises(ValueError):
            Rectangle(7, -14)

        with self.assertRaises(ValueError):
            Rectangle(7, 14, -21)

        with self.assertRaises(ValueError):
            Rectangle(7, 14, 21, -28)

        with self.assertRaises(ValueError):
            Rectangle(0, 7)
        
        with self.assertRaises(ValueError):
            Rectangle(7, 0)
if __name__== "__main__":
    unittest.main()
