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

def filtra_nodo_raiz(actual, nodo):
    """ Imprime sólo los nodos que son igual a node """
    if nodo:
        if actual.nodeName == nodo:
            print(actual.nodeName)
        else:
            pass
    else:
        print(actual.nodeName)

def filtra_hijos(hijo, nodo, l):
    """ Imprime sólo los hijos que son igual a nodo """
    if nodo:
        if hijo.nodeName == nodo:
            print("   "*l + "|-", hijo.nodeName)
        else:
            pass
    else:
        print("   "*l + "|-", hijo.nodeName)

def filtra_hijos_data(raiz, data, nodo, l):
    """ Imprime sólo las data de los hijos que son igual a nodo """
    if nodo:
        if raiz.nodeName == nodo:
            print("   "*l + "|-", data)
        else:
            pass
    else:
        print("   "*l + "|-", data)

def imprime_hijos(nodo, node, l=0):
    """
    Imprime el contenido de un nodo en la salida estándar
    """
    if nodo.attributes:
        if node:
            if nodo.nodeName == node:
                imprime_atributos(nodo, l)
            else:
                pass
        else:
            imprime_atributos(nodo, l)
            
    for hijo in nodo.childNodes:
        if hijo.nodeName == "#text":
            if hijo.data.strip() != "":
                filtra_hijos_data(nodo, hijo.data, node, l)
                # print("   "*l, "|-", hijo.data)
        else:
            filtra_hijos(hijo, node, l)
            imprime_hijos(hijo, node, l+1)


@click.command()
@click.option("--raw", is_flag=True,
    help="Imprime el contenido del archivo sin modificación alguna")
@click.option("--node", type=str,
    help="Muestra solamente los nodos cuyo nombre esta dado por TEXT")
@click.argument("pathfile", type=click.Path(exists=True), required=True)
def catxml(raw, node, pathfile):
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
        filtra_nodo_raiz(raiz, node)
        imprime_hijos(raiz, node)
                
            
if __name__ == "__main__":
    catxml()