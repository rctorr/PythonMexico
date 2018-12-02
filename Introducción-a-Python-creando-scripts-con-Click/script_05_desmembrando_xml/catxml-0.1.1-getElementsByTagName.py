#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import click
from xml.dom import minidom

def printChildren(node, level = 0):
    for child in node.childNodes:
        if child.nodeName != "#text":
            print("\t"*level + "|_" + child.nodeName)
            printChildren(child, level + 1)

@click.command()
@click.option("--raw", is_flag=True, help="Imprime el XML en formato crudo")
@click.option("--node", type=str, help="Imprime el árbol del nodo especificado")
@click.argument("filepath", type=click.Path(exists=True))
def catxml(raw, filepath, node):
    """
    Despliega el contenido de un XML
    """
    if raw:
        with open(filepath) as stream:
            for row in stream:
                print(row, end="")
    else:
        dom = minidom.parse(filepath)
        if node != None:
            nodes = dom.getElementsByTagName(node)
            for child in nodes:
                print(child.nodeName)
                printChildren(child)
            pass
        else:
            root = dom.childNodes[0]
            print(root.nodeName)
            printChildren(root)

if __name__ == '__main__':
    catxml()
