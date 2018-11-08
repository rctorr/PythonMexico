#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import random

@click.command()
@click.option("--len", default=8, type=int, help="Longitud de la clave")
@click.option("--n", default=1, type=int,
        help="Indica el número de claves a generar")
def genpass(len, n):
    """
    Genera una clave segura usando como base el alfabeto inglés en
    mayúsculasx, minúsculas y digitos.
    """
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos = "01234567890"

    for i in range(n):
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
