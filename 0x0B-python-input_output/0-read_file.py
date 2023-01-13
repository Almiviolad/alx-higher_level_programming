#!/usr/bin/python3
"""Functoon to openand print the content of a file"""


def read_file(filename=""):
    """Reads and print line content of a file
    Args:
        filename: The name of the fike to be read
        """
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end = "")
