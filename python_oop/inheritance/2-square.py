#!/usr/bin/env python3
"""Defines a Square class inheriting from Rectangle with custom str representation."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle inheritance."""

    def __init__(self, size):
        """Initializes a square with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the print representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
