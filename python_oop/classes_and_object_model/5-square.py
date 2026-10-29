#!/usr/bin/env python3
"""Definición de la clase Square con método de impresión."""


class Square:
    """Representa un cuadrado con validación de tamaño y capacidad de impresión."""

    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado con un tamaño opcional.

        Args:
            size (int): El tamaño del cuadrado (por defecto 0).
        """
        self.size = size

    @property
    def size(self):
        """Recupera el tamaño actual del cuadrado.

        Returns:
            int: El tamaño del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida el tamaño del cuadrado.

        Args:
            value (int): El nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula y devuelve el área actual del cuadrado.

        Returns:
            int: El área del cuadrado (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Imprime en la salida estándar el cuadrado usando el carácter '#'."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
