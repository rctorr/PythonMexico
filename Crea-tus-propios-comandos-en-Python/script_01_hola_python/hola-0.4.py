#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aquí se importan módulos o librerías
import sys

def help():
    """ Imprime la ayuda del script en la salida estándar """
    print("""
Sintaxis:
    hola.py [--help] tuNombre

Imprime en la salida estándar el saludo incluyendo tuNombre

Opciones:
--help Imprime en la salida estándar esta ayuda
    """)

# Se define una función, en este caso la función main(), aunque en
# Python no es necesaria se usa y define por convención y organización
# del código.
def main(argv):
    """ Función principal del script """
    # Verificamos si tenemos tenemos un argumento
    if len(argv) < 2:
        # No tenemos datos para continuar, enviamos la ayuda
        help()
        # Terminamos el script
        sys.exit(0)
    # Buscamos la opción --help
    if "--" in argv[1]:
        help()
        sys.exit(0)

    # Si llegamos hasta aquí, entonces tenemos datos para continuar
    print(("Hola {}!".format(argv[1])).upper())

# Este if permite usar este script como un comando desde el shell o
# como un módulo desde otro script en Python.
if __name__ == "__main__":
    main(sys.argv)
