#!/usr/bin/python3
"""Defines a class based on BaseGeometry class"""


class BaseGeometry:
    """class about the geometry of shapes"""

    def area(self):
        """
        raises an exception ara is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): name of value in mmessage to be raised
           value (int): integer t be validated
        Raises:
            TypeError: if value is not int
            ValueError: if valie is less than or equal to zero
        """
        if not(isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
