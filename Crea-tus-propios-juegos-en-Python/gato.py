#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este script es para jugar el juego de gato por turnos con un usuario humano
y un usuario inhumano.

El juego consta de un tablero de 9 casillas

0 * * *
1 * * *
2 * * *
  0 1 2

Para elegir una casilla se usa el sistema de coordenadas, donde la
casilla (0, 0) es la de la esquina superior izquierda.

El usuario siempre inicia primero
"""

# 1. Imprimir tablero
# 2. Es turno de usuario: juega_usuario
# 3. Es turno de ia: juega_ia
# 4. Regresar a 1


import random

def imprime(tablero):
    """
    Imprime el tablero en la salida estándar
    """
    for i, linea in enumerate(tablero):
        linea = ["o" if c==1 else "x" if c==2 else "*" for c in linea]
        linea = " ".join(linea)
        print(i, linea)
    print("  0 1 2")
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
            tablero[ren][col] = 2
            jugada = True

def gana(tablero, n):
    """
    Regresa True si el jugador n ha ganado, False en caso contrario
    """
    val = n * 3
    for ren in tablero:
        ren = [c for c in ren if c == n]
        if len(ren) == 3:
            return True
    for i in range(3):
        col = [ren[i] for ren in tablero if ren[i] == n]
        if len(col) == 3:
            return True
    diag1 = [ren[i] for i, ren in enumerate(tablero) if ren[i] == n]
    if len(diag1) == 3:
        return True
    diag2 = [ren[2-i] for i, ren in enumerate(tablero) if ren[2-i] == n]
    if len(diag2) == 3:
        return True

    return False

def main():
    """
    Función principal del juego de gato
    """
    tablero = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    turno = 0 # 0 turno de usuario, 1 turno de ia
    fin = False # Define cuando ha terminado el juego

    print()
    print("Juego de Gato")
    print("-"*13)

    while not fin:
        imprime(tablero)
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
            if gana(tablero, 2):
                fin = True
                print("-"*13)
                print("La IA gana!")
                print("-"*13)

    imprime(tablero)

if __name__ == "__main__":
    main()

