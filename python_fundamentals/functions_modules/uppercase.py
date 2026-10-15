#!/usr/bin/env python3
"""Módulo que contiene la función uppercase para convertir cadenas a mayúsculas."""


def uppercase(n_str):
    """Imprime una cadena en mayúsculas utilizando lógica ASCII y .format()."""
    result = "".join(
        chr(ord(c) - 32) if ord('a') <= ord(c) <= ord('z') else c
        for c in n_str
    )
    print("{}".format(result))
