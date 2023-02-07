#!/usr/bin/python3
"""
   Define a function that check if an object is an instance of a class if an inheritance is direct or indirect
"""
def is_kind_of_class(obj, a_class):
    """
    checks if an obj inherits directly from a class
    Args:
        obj: The object to checked
        a_class: The class to be checked
"""
    if isinstance(obj, a_class):
        return True
    return False
