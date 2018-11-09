#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
import time

@click.command()
@click.argument("path", default=".")
def l(path):
    """
    Imprime en la salida estándar la lista de archivos de PATH, si PATH
    no se indica, entonces se imprime la lista de archivos del directorio
    actual.
    """
    lista = os.listdir(path)
    for item in lista:
        print("{:30} {:5} {:12} {}".format(
            item,
            os.path.splitext(item)[1],
            os.path.getsize(os.path.join(path, item)),
            time.strftime("%d-%m-%Y %H:%M", time.localtime(os.path.getctime(os.path.join(path, item))))
        ))


if __name__ == "__main__":
    l()
