#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
En esta v0.2.1 la lista se imprime en formato html pero incluyendo una
página completa y estilos.
"""

import click
import os
import time

def imprime_html(path, lista):
    """
    Imprime la lista en la salida estándar en formato html generando
    una página completa y permitiendo el uso del archivo de estilos
    css/main.css
    """
    plantilla = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Lista de archivos en formato HTML con estilos</title>
    <link rel="stylesheet" type="text/css" href="css/main.css" />
</head>
<body>
    <h2>Lista de archivos en HTML5 y CSS3 generada desde un script en
    Python</h2>
    <hr />
    <table>
        <tr>
            <th>Nombre</th>
            <th>Extensión</th>
            <th>Tamaño</th>
            <th>Fecha</th>
        </tr>
        {}
    </table>
</body>
</html>
    """
    info = ""
    # Aquí genera la lista, pero en formato html
    for item in lista:
        info += "        <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(
            item,
            os.path.splitext(item)[1],
            os.path.getsize(os.path.join(path, item)),
            time.strftime("%d-%m-%Y %H:%M", time.localtime(os.path.getctime(os.path.join(path, item))))
        )
    # Se agrega la info a la plantilla
    html = plantilla.format(info)
    # Después de la lista se imprime en la salida estándar
    print(html)


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
    if to_html:
        imprime_html(path, lista)
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
