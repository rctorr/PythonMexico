#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.argument("tunombre")
def hola(tunombre):
    """
    Escribe el mensaje:

        Hola TUNOMBRE desde click!

    y además verifica que el usuario proporcione opciones válidas.
    """
    print("Hola {} desde click!".format(tunombre))


if __name__ == "__main__":
    hola()
