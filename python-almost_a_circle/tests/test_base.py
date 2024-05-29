#!/usr/bin/python3
""" Module: contains unittests for Base class """
import unittest
from models.base import Base


class Testbaseclass(unittest.TestCase):
    """ Unit testing for Base class """
    def test_auto_base(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)
    
    def test_assigned_base(self):
        base1 = Base(21)
        self.assertEqual(base1.id, 21)

    def test_to_json_str(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 21}]), '[{"id": 21}]')
    
    def test_from_json(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.from_json_string('[{"id": 21}]'), [{"id": 21}])

if __name__== "__main__":
    unittest.main()
