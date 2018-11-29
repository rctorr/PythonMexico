#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from xml.dom import minidom

def imprime_atributos(nodo, l):
    """
    Imprime los atributos de un nodo
    """
    for nom, val in nodo.attributes.items():
        print("   "*l + "|-", nom, "=", val)

def imprime_hijos(nodo, l=0):
    """
    Imprime el contenido de un nodo en la salida estándar
    """
    if nodo.attributes:
        imprime_atributos(nodo, l)
    for hijo in nodo.childNodes:
        if hijo.nodeName == "#text":
            if hijo.data.strip() != "":
                print("   "*l, "|-", hijo.data)
        else:
            print("   "*l + "|-", hijo.nodeName)
            imprime_hijos(hijo, l+1)


@click.command()
@click.option("--raw", is_flag=True,
    help="Imprime el contenido del archivo sin modificación alguna")
@click.argument("pathfile", type=click.Path(exists=True), required=True)
def catxml(pathfile, raw):
    """
    Imprime en la salida estándar el contenido del archivo xml
    indicado por PATHFILE
    """
    if raw:
        with open(pathfile) as f:
            for linea in f:
                print(linea, end="")
    else:
        dom = minidom.parse(pathfile)
        raiz = dom.childNodes[0]
        print(raiz.nodeName)
        imprime_hijos(raiz)
                
            
if __name__ == "__main__":
    catxml()