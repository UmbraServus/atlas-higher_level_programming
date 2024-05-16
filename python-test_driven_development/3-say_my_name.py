#!/usr/bin/python3
"""" method that prints a string with first and last name """

def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name>

        args:
            first_name(str): first name
            last_name(str): last name

        raises:
            TypeError: First and Last name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
