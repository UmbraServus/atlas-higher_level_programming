#!/usr/bin/python3
""" module is base class """


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """methods/setters/getters"""

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json string representation of list dictionaries"""
        import json
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
