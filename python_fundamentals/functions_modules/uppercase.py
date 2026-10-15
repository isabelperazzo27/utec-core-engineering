#!/usr/bin/env python3
"""Módulo que contiene la función uppercase para convertir cadenas a mayúsculas."""


def uppercase(n_str):
    """Imprime una cadena en mayúsculas utilizando lógica ASCII."""
    for c in n_str:
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()
