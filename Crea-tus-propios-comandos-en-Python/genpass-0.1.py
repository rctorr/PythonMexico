#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import random

@click.command()
@click.option("--len", default=8, type=int, help="Longitud de la clave")
def genpass(len):
    """
    Genera una clave segura usando como base el alfabeto inglés en
    mayúsculasx, minúsculas y digitos.
    """
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos = "01234567890"

    clave = random.choice(minusculas)
    clave += random.choice(mayusculas)
    clave += random.choice(digitos)

    k = len - 3

    faltan = random.choices(minusculas+mayusculas+digitos, k=k)

    clave = list(clave) + faltan
    random.shuffle(clave)
    clave = "".join(clave)

    print(clave)

if __name__ == "__main__":
    genpass()
