#!/usr/bin/env python3
"""Definición de la clase Rectangle con cálculo de área y perímetro."""


class Rectangle:
    """Representa un rectángulo con ancho, alto, área y perímetro."""

    def __init__(self, width=0, height=0):
        """Inicializa un nuevo rectángulo con ancho y alto opcionales.

        Args:
            width (int): El ancho del rectángulo (por defecto 0).
            height (int): El alto del rectángulo (por defecto 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Recupera el ancho actual del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece y valida el ancho del rectángulo."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Recupera el alto actual del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece y valida el alto del rectángulo."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula y devuelve el perímetro del rectángulo.

        Returns:
            int: El perímetro, o 0 si width o height son 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
