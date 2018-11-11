#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este script es para jugar el juego de gato por turnos con un usuario humano
y un usuario inhumano.

El juego consta de un tablero de 9 casillas

  0 1 2
0 * * *
1 * * *
2 * * *

Para elegir una casilla se usa el sistema de coordenadas, donde la
casilla (0, 0) es la de la esquina superior izquierda.

El usuario siempre inicia primero
"""

# 1. Imprimir tablero
# 2. Es turno de usuario: juega_usuario
# 3. Es turno de ia: juega_ia
# 4. Regresar a 1


import random

def imprime(tablero, simb1, simb2):
    """
    Imprime el tablero en la salida estándar
    """
    print("  0 1 2")
    simbs = "_"+simb1+simb2
    for i, linea in enumerate(tablero):
        linea = [simbs[c] for c in linea]
        linea = " ".join(linea)
        print(i, linea)
    print()

def juega_usuario(tablero):
    """
    Realiza el procedimiento de una jugada de usuario
    """
    print("Juega usuario!")
    val = input("Elige columna [0,1,2] ?")
    col = int(val)
    val = input("Elige renglón[0,1,2] ?")
    ren = int(val)
    print()
    if tablero[ren][col] == 0:
        tablero[ren][col] = 1
        return True
    else:
        print("Casilla inválida!")
        return False

def juega_ia(tablero):
    """
    Realiza el procedimiento de una jugada de ia
    """
    jugada = False
    print("Juega IA")
    while not jugada:
        col = random.randrange(3)
        ren = random.randrange(3)
        if tablero[ren][col] == 0:
            tablero[ren][col] = -1
            jugada = True

def gana(tablero, n):
    """
    Regresa True si el jugador n ha ganado, False en caso contrario
    """
    # Busca gato en horizontales
    for ren in tablero:
        if abs(sum(ren)) == 3 and n in ren:
            return True
    # Busca gato en verticales
    for col in zip(*tablero):
        if abs(sum(col)) == 3 and n in col:
            return True
    # Busca gato en diagonal 1
    diag1 = [ren[i] for i, ren in enumerate(tablero)]
    if abs(sum(diag1)) == 3 and n in diag1:
        return True
    # Busca gato en diagonal 2
    diag2 = [ren[2-i] for i, ren in enumerate(tablero)]
    if abs(sum(diag2)) == 3 and n in diag2:
        return True

    return False

def main():
    """
    Función principal del juego de gato
    """
    tablero = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    turno = 0  # 0 turno de usuario, 1 turno de ia
    fin = False  # Define cuando ha terminado el juego
    simb1 = "o"  # Símbolo del jugador 1, de momento el usuario
    simb2 = "x"  # Símbolo del jugador 2, de momento la IA

    print()
    print("Juego de Gato")
    print("-"*13)

    while not fin:
        imprime(tablero, simb1, simb2)
        if turno == 0:
            if juega_usuario(tablero):
                turno = 1
                if gana(tablero, 1):
                    print("-"*13)
                    print("El usuario gana!")
                    print("-"*13)
                    fin = True
        else:
            juega_ia(tablero)
            turno = 0
            if gana(tablero, -1):
                fin = True
                print("-"*13)
                print("La IA gana!")
                print("-"*13)

    imprime(tablero, simb1, simb2)

if __name__ == "__main__":
    main()
