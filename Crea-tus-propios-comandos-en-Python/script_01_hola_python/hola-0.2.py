#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aquí se importan módulos o librerías
import sys

# Se define una función, en este caso la función main(), aunque en
# Python no es necesaria se usa y define por convención y organización
# del código.
def main(argv):
    """ Función principal del script """
    # La impresión de datos a la salida estándar se realiza con la
    # función print()
    # Una forma de controlar el formato es por medio del método
    # "".format() que todo string tiene.
    print("Hola {}!".format(argv[1]))

# Este if permite usar este script como un comando desde el shell o
# como un módulo desde otro script en Python.
if __name__ == "__main__":
    main(sys.argv)
