#!/usr/bin/env python3
"""Módulo para imprimir y devolver el último dígito de un número."""


def print_last_digit(number):
    """Imprime y devuelve el último dígito de un número."""
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
