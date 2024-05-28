#!/usr/bin/python3
""" module is base class """
import json
import os


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
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """returns a list of the json str representation."""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the json str representation to classname.json """
        dict_list = []
        file = cls.__name__ + ".json"
        with open(file, "w") as f:
            if list_objs is None:
                json_str = cls.to_json_string(dict_list)
                f.write(json_str)
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(dict_list)
                f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ creates a dummy instance of class and updates it """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod    
    def load_from_file(cls):
        """ loads a json str from file then returns an instance of the
            object contained in the file."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_str = file.read()
            list_dicts = cls.from_json_string(json_str)
            return [cls.create(**d) for d in list_dicts]