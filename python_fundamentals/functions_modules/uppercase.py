#!/usr/bin/env python3
"""Módulo para convertir cadenas a mayúsculas."""


def uppercase(n_str):
    """Imprime una cadena en mayúsculas."""
    result = "".join(
        chr(ord(c) - 32)
        if ord('a') <= ord(c) <= ord('z')
        else c
        for c in n_str
    )
    print("{}".format(result))
