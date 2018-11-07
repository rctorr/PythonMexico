#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from collections import OrderedDict
import csv
import os
from pyexcel_xls import save_data
import time
import sys

@click.command()
@click.option("--tocsv", is_flag=True,
        help="Imprime la lista de archivos en formato CSV en la salida\
        estándar")
@click.option("--toxls", is_flag=True,
        help="Guarda la lista de archivos en formato XLS en el archivo\
        lista.xls en el directorio actual")
@click.argument("path", default=".")
def l(tocsv, toxls, path):
    """
    Imprime en la salida estándar la lista de archivos de PATH, si PATH
    no se indica, entonces se imprime la lista de archivos del directorio
    actual.
    """
    lista = os.listdir(path)
    csv_out = csv.writer(sys.stdout)
    xls_do = OrderedDict() # Un diccionario en Python con orden
    if toxls:
        # Se inicia el diccionario con el nombre de la hoja con
        # una línea con el nombre de las columnas
        xls_do.update(
                {"Archivos":[["Nombre", "Extensión", "Tamaño", "Fecha"]]})
        # Generamos y agregamos cada archivos, uno por línea
        for item in lista:
            linea = [
                item,
                os.path.splitext(item)[1],
                os.path.getsize(os.path.join(path, item)),
                time.strftime("%d-%m-%Y %H:%M", time.localtime(os.path.getctime(os.path.join(path, item))))
            ]
            xls_do["Archivos"].append(linea)
        # Guardamos los datos
        save_data("lista.xls", xls_do)
        print("Se creó el archivo lista.xls en el directorio actual")
    else:
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
