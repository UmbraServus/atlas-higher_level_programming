#!/usr/bin/python3
""" appends to a file"""


def append_write(filename="", text=""):
    """opens and appends to a file

        args:
            filename: name of file
            text: text to be added to file
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
