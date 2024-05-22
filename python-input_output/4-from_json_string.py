#!/usr/bin/python3
"""JSON string module"""


def from_json_string(my_str):
    """Returns an obj represented by a JSON string"""

    import json
    return json.loads(my_str)
