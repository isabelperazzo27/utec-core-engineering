#!/usr/bin/env python3
"""Defines a Rectangle class inheriting from BaseGeometry with area and str."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry inheritance."""

    def __init__(self, width, height):
        """Initializes a rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
