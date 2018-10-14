#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import csv
import os
import time
import sys

@click.command()
@click.option("--tocsv", is_flag=True, help="Imprime la lista de archivos en formato CSV")
@click.argument("path", default=".")
def l(tocsv, path):
    """
    Imprime en la salida estándar la lista de archivos de PATH, si PATH
    no se indica, entonces se imprime la lista de archivos del directorio
    actual.
    """
    lista = os.listdir(path)
    csv_out = csv.writer(sys.stdout)
    for item in lista:
        if tocsv:
            linea = [
                item,
                os.path.splitext(item)[1],
                os.path.getsize(os.path.join(path, item)),
                time.strftime("%d-%m-%Y %H:%M", time.localtime(os.path.getctime(os.path.join(path, item))))
            ]
            csv_out.writerow(linea)
        else:
            print("{:30} {:5} {:12} {}".format(
                item,
                os.path.splitext(item)[1],
                os.path.getsize(os.path.join(path, item)),
                time.strftime("%d-%m-%Y %H:%M", time.localtime(os.path.getctime(os.path.join(path, item))))
            ))


if __name__ == "__main__":
    l()
