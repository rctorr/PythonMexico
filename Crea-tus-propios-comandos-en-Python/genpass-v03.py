#!/usr/bin/python3

import click
import random

@click.command()
@click.option("--len", default=8, type=int, help="longitud de la clave")
@click.option("--num", default=1, type=int, help="cantidad de claves")
@click.option("--sim", default="", type=str, help="caracteres")
def genpass(len, num, sim):
    """
    Generar una clave segura utilizando el alfanumerico ingles en mayusculas, minusculas y digitos
    """
    minusculas="abcdefghijklmnopqrstuvwxyz"
    mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos="0123456789"
    
    for i in range(num):
        clave =random.choice(minusculas)
        clave+=random.choice(mayusculas)
        clave+=random.choice(digitos)
        clave+=random.choice(sim)
        k=len-3
        faltan=random.choices(minusculas+mayusculas+digitos, k=k)
        clave=list(clave)+faltan
        random.shuffle(clave)
        clave="".join(clave)
        print(clave)

if __name__ == "__main__":
    genpass()
