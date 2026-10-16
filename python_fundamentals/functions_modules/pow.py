#!/usr/bin/env python3
"""Módulo para calcular la potencia de un número sin usar **."""


def pow(a, b):
    """Calcula a elevado a la potencia b usando un bucle."""
    if b == 0:
        return 1
    
    result = 1
    exponent = abs(b)
    
    for _ in range(exponent):
        result *= a
        
    if b < 0:
        return 1 / result
    return result
