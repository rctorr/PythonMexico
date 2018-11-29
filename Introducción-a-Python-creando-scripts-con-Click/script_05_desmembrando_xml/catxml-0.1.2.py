#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from xml.dom import minidom

def filtra_attr(nom, val, attr, l):
    """ Imprime sólo los atributos que son igual a attr """
    if attr:
        if nom == attr:
            print("   "*l + "|-", nom, "=", val)
        else:
            pass
    else:
        print("   "*l + "|-", nom, "=", val)

def imprime_atributos(nodo, attr, l):
    """
    Imprime los atributos de un nodo
    """
    for nom, val in nodo.attributes.items():
        filtra_attr(nom, val, attr, l)

def filtra_nodo_raiz(actual, nodo, attr):
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

def imprime_hijos(nodo, node, attr, l=0):
    """
    Imprime el contenido de un nodo en la salida estándar
    """
    if nodo.attributes:
        if node:
            if nodo.nodeName == node:
                imprime_atributos(nodo, attr, l)
            else:
                pass
        else:
            imprime_atributos(nodo, attr, l)
            
    for hijo in nodo.childNodes:
        if hijo.nodeName == "#text":
            if hijo.data.strip() != "":
                filtra_hijos_data(nodo, hijo.data, node, l)
                # print("   "*l, "|-", hijo.data)
        else:
            filtra_hijos(hijo, node, l)
            imprime_hijos(hijo, node, attr, l+1)


@click.command()
@click.option("--raw", is_flag=True,
    help="Imprime el contenido del archivo sin modificación alguna")
@click.option("--node", type=str,
    help="Muestra solamente los nodos cuyo nombre esta dado por TEXT")
@click.option("--attr", type=str,
    help="Muestra solamente los atributos cuyo nombre esta dado por TEXT")
@click.argument("pathfile", type=click.Path(exists=True), required=True)
def catxml(raw, node, attr, pathfile):
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
        filtra_nodo_raiz(raiz, node, attr)
        imprime_hijos(raiz, node, attr)
                
            
if __name__ == "__main__":
    catxml()