#!/usr/bin/env python3
"""Módulo que contiene la función islower para verificar letras minúsculas."""


def islower(c):
    """Devuelve True si c es una letra minúscula, False en caso contrario.
    Utiliza lógica ASCII mediante la función ord().
    """
    return ord('a') <= ord(c) <= ord('z')
