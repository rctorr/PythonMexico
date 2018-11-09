#!/usr/bin/python3
# -*- coding: utf-8 -*-

import click
import random

@click.command()
@click.option("--len", default=8, type=int, help="Longitud de la clave. Por omisión es 8.")
@click.option("--num", default=1, type=int, help="Cantidad de claves. Por omisión es 1.")
@click.option("--sim", default="", type=str, help="Símbolos a incluir en la clave. Ej: '!@#$%'")
def genpass(len, num, sim):
    """
    Generar una clave segura utilizando el alfanumerico inglés en mayúsculas, minúsculas y dígitos
    """
    minusculas="abcdefghijklmnopqrstuvwxyz"
    mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos="0123456789"
    
    for i in range(num):
        clave = random.choice(minusculas)
        clave += random.choice(mayusculas)
        clave += random.choice(digitos)
        alfabeto = minusculas + mayusculas + digitos
        k=len-3
        if sim:
            clave += random.choice(sim)
            alfabeto += sim
            k -= 1
        faltan = random.choices(alfabeto, k=k)
        clave = list(clave) + faltan
        random.shuffle(clave)
        clave = "".join(clave)
        print(clave)

if __name__ == "__main__":
    genpass()