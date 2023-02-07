#!/usr/bin/python3
"""
   Defines a function to check if an object ia a instance of a class, direct or indirect inheritance
"""
def inherits_from(obj, a_class):
    """
    Checks if an obj inherits directly or indirectly from a class
    Args:
        obj: The object
        a_class: The class that is to be cimpared
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
