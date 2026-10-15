#!/usr/bin/env python3
"""Módulo que contiene la función uppercase para convertir cadenas a mayúsculas."""


def uppercase(s):
    """Imprime una cadena en mayúsculas utilizando lógica ASCII."""
    result = ""
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result)
