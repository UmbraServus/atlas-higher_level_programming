#!/usr/bin/python3
"""save to json file module"""

def save_to_json_file(my_obj, filename):
    """saves an json obj to file as a string"""

    with open(filename, 'w', encoding="utf-8") as f:
        import json
        f.write(json.dumps(my_obj))
        