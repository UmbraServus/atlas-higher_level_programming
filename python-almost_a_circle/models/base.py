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
