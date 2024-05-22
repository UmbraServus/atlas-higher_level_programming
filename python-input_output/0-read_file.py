#!/usr/bin/python3
"""Module: This module is for opening and reading a file"""


def read_file(filename=""):
    """opens and reads file using with.

        args:
            filename: name of the file to be opened"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
