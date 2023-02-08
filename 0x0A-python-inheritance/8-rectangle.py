#!/usr/bin/python3
"""Defines a rectangle shape"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeomery):
    """Defines.a rectangle shpe class"""

    def __init__(self, width, height):
        """initialises a new rectangle

        Args:
            width (int):Width of the new rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
