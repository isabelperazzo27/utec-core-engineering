#!/usr/bin/env python3
"""Módulo para importar y ejecutar la función add desde add_0.py."""

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
