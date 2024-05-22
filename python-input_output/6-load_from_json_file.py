#!/usr/bin/python3
"""load from json file module"""


def load_from_json_file(filename):
    """creates and obj from json file"""

    with open(filename, mode="r", encoding="utf-8") as f:
        import json
        return json.loads(f)
