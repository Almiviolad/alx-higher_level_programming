#!/usr/bin/python3
"""
   Define a function of direct and indirect inheritance """


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
