#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.option("--repetir", default=1, type=int, help="Imprime N veces el mensaje")
@click.argument("tunombre")
def hola(repetir, tunombre):
    """
    Escribe el mensaje:

        Hola TUNOMBRE desde click!

    y además verifica que el usuario proporcione opciones válidas.
    """
    for i in range(repetir):
        print("Hola {} desde click!".format(tunombre))

    # print("Valor de repetir: {}, {}".format(repetir, type(repetir)))


if __name__ == "__main__":
    hola()
