#!/usr/bin/python3
"""JSON string module"""


def to_json_string(my_obj):
    """Returns the JSON string representation of an object"""
    
    import json
    return json.dumps(my_obj)