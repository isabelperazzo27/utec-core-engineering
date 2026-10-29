#!/usr/bin/env python3
"""Definición de clase Square con tamaño, posición e impresión."""


class Square:
    """Representa un cuadrado con tamaño, posición y

    representación en cadena.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un nuevo cuadrado con tamaño

        y posición opcionales.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Recupera el tamaño actual del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida el tamaño del cuadrado."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Recupera la posición actual del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece y valida la posición del cuadrado."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Calcula y devuelve el área actual del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """Imprime en la salida estándar el cuadrado con '#' y posición."""
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            print("\n" * (self.__position[1] - 1))
        for _ in range(self.__size):
            spaces = " " * self.__position[0]
            hashes = "#" * self.__size
            print("{}{}".format(spaces, hashes))

    def __str__(self):
        """Define la representación en cadena del objeto Square."""
        if self.__size == 0:
            return ""
        lines = []
        if self.__position[1] > 0:
            lines.append("\n" * self.__position[1])
        for _ in range(self.__size):
            spaces = " " * self.__position[0]
            hashes = "#" * self.__size
            lines.append("{}{}".format(spaces, hashes))
        return "\n".join(lines)
