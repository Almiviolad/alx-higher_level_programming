#!/usr/bin/python3
"""
Define a class checking function
"""
def is_kind_of_class(obj, a_class):
    """check if an object is an instance of a class
    Args:
        obj: The object
        a_class: Tge class to be checked
    """
    if type(obj) == a_class:
        return True
    return False
