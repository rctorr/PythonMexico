#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import random

@click.command()
@click.option("--len", default=8, type=int, help="Longitud de la clave")
@click.option("--n", default=1, type=int,
        help="Indica el número de claves a generar")
@click.option("--with-simb", is_flag=True,
        help="Indica si se incluyen los símbolos como parte de la clave, por omosión no.")
def genpass(len, n, with_simb):
    """
    Genera una clave segura usando como base el alfabeto inglés en
    mayúsculasx, minúsculas y digitos.
    """
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos = "01234567890"
    simbolos = "!@#$%&()=+-:;.,"

    for i in range(n):
        clave = random.choice(minusculas)
        clave += random.choice(mayusculas)
        clave += random.choice(digitos)

        k = len - 3

        alfabeto = minusculas+mayusculas+digitos

        if with_simb:
            clave += random.choice(simbolos)
            alfabeto += simbolos
            k -= 1

        faltan = random.choices(alfabeto, k=k)

        clave = clave.split() + faltan
        random.shuffle(clave)
        clave = "".join(clave)

        print(clave)

if __name__ == "__main__":
    genpass()
