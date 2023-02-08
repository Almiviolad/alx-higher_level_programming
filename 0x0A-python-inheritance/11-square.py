#!/usr/bin/python3
"""Defines a square from a base class rectangle"""
Rectangle = __import___('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Repreesents a square"""
    def __init__(self, size):
        """initializses a new square
        Args:
            size (int): size of the new square
        """
    self.integer_validator("size", size)
    super().__init__(size, size)
    self.__size = size

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        """Return the print() and str() representation of a square."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
