#!/usr/bin/python3
"""Define a class base"""


class Base:

    """Represnt the bas for model class in thus project
    Attributes:
        __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initilauses the class cinstructor
        Arguments:
            id( int)
        """
        if is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
