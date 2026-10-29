#!/usr/bin/env python3
"""Defines a Square class."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
