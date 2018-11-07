#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
En esta v0.2 del script le vamos agregar la opción --to-html para
poder imprimir las lista de archivos en la salida estándar pero en
formato html.
"""

import click
import os
import time

@click.command()
@click.option("--to-html", is_flag=True, help="Imprime la lista en formato html")
@click.argument("path", default=".")
def l(to_html, path):
    """
    Imprime en la salida estándar la lista de archivos de PATH, si PATH
    no se indica, entonces se imprime la lista de archivos del directorio
    actual.
    """

    # Se obtiene la lista de archivos de path
    lista = os.listdir(path)

    # Verificamos si el usuario quiere la salida en formato html
    if to_html == True:
        # Se imprime el inicio y la cabezera de tabla
        print("""
    <table>
    <tr><th>Nombre</th><th>Extensión</th><th>Tamaño</th><th>Fecha</th></tr>
        """)
        # Aquí imprimimos la lista, pero en formato html
        for item in lista:
            print("    <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                item,
                os.path.splitext(item)[1],
                os.path.getsize(os.path.join(path, item)),
                time.strftime("%d-%m-%Y %H:%M", time.localtime(os.path.getctime(os.path.join(path, item))))
            ))
        # Después de la lista se imprime el fin de tabla
        print("</table>")
        print()
    else:
    # Si no, entonce imprime la lista en formato texto en columnas
        for item in lista:
            print("{:30} {:5} {:12} {}".format(
                item,
                os.path.splitext(item)[1],
                os.path.getsize(os.path.join(path, item)),
                time.strftime("%d-%m-%Y %H:%M", time.localtime(os.path.getctime(os.path.join(path, item))))
            ))


if __name__ == "__main__":
    l()
