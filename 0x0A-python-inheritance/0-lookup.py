#!/usr/bin/python3
"""
The definition of the function that lokup the method and attributeof a class
"""
def lookup(obj):
    """Returns ge list of atributes and methods of class
    Args:
        obj: He class whose methods amd atributes are to bereturned
    """
    return (dir(obj))
