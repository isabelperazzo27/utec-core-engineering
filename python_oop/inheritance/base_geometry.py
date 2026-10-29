#!/usr/bin/env python3
"""Defines a base geometry class with area and validation methods."""


class BaseGeometry:
    """Represents base geometry operations and validations."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter value to ensure it is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
