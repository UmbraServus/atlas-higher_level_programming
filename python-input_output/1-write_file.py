#!/usr/bin/python3
""" writes to a file"""


def write_file(filename="", text=""):
    """opens and writes to a file

        args:
            filename: name of file
            text: text to be added to file
    """


    with open(filename, 'w', encoding="utf-8") as f:
       return f.write(text)
