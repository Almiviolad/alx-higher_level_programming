#!/usr/bin/python3
"""Prints fisrt and last name"""


def say_my_name(first_name, last_name=""):
    """
    usage:
        prints the first and last nam
    args:
        first_name
        last_name
    raises:
        Typeerror(if the arg is not a string)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if(last_name == ""):
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
