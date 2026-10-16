#!/usr/bin/env python3
"""Módulo para calcular la potencia de un número sin usar **."""


def pow(a, b):
    """Calcula a elevado a la potencia b usando un bucle."""
    result = 1
    if b < 0:
        base = 1 / a
        exponent = -b
    else:
        base = a
        exponent = b

    for _ in range(exponent):
        result *= base
    return result
