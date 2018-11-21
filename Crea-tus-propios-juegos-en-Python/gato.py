#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este script es para jugar el juego de gato por turnos con un usuario humano
y un usuario inhumano.

El juego consta de un tablero de 9 casillas

  0 1 2
0 . . . 
1 . . .
2 . . .

Para elegir una casilla se usa el sistema de coordenadas, donde la
casilla (0, 0) es la de la esquina superior izquierda.

Desarrollo

El tablero en una lista de 3 listas de 3 elementos los valores posibles
son los siguientes:
    0 - Indica que la casilla está vacía y es el estado inicial
    1 - Indica que es una casilla ocupada por una tirada del Humano
   -1 - Indica que es una casilla ocupara por una tirada de la IA
"""

import random

class Gato:
    def __init__(self):
        self.tablero = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        self.humano = 1
        self.ia = -1
        self.fin_de_juego = False

    def imprime_tablero(self):
        print()
        print("  0 1 2")
        for i, ren in enumerate(self.tablero):
            print(i, " ".join([self.simbs[v] for v in ren]))
        print()

    def humano_elige(self):
        print()
        resp = input("Elige 'x' o 'o' ? ")
        if resp.lower() == "x":
            self.simbs = [".", "x", "o"]
        else:
            self.simbs = [".", "o", "x"]
        print()

    def tirada(self, p, j):
        self.tablero[p[0]][p[1]] = j

    def juega_humano(self):
        print()
        resp = input("Turno humano (ren, col) ? ")
        p = [int(v) for v in resp.split(",")]
        self.tirada(p, self.humano)
        print()

    def casillas_libres(self):
        return [(i, j) for j in random.sample(range(3), 3)
                for i in random.sample(range(3), 3)
                if self.tablero[i][j] == 0]

    def juega_ia(self):
        print("\nTurno de la IA!\n")
        casillas = self.casillas_libres()

        for c in casillas:
            self.tirada(c, self.ia)
            if self.gana(self.ia):
                return
            else:
                self.tirada(c, 0)
        for c in casillas:
            self.tirada(c, self.humano)
            if self.gana(self.humano):
                self.tirada(c, self.ia)
                return
            else:
                self.tirada(c, 0)
        for c in casillas:
            if c[0] in [0, 2] and c[1] in [0, 2]:
                self.tirada(c, self.ia)
                return
        if (1, 1) in casillas:
            self.tirada((1, 1), self.ia)
            return

        self.tirada(casillas[0], self.ia)



    def gana(self, j):
        for ren in self.tablero:
            if sum(ren) == 3 * j:
                return True
        for col in zip(*self.tablero):
            if sum(col) == 3 * j:
                return True
        diag1 = [ren[i] for i, ren in enumerate(self.tablero)]
        if sum(diag1) == 3 * j:
            return True
        diag2 = [ren[2-i] for i, ren in enumerate(self.tablero)]
        if sum(diag2) == 3 * j:
            return True

    def imprime_resultado(self):
        print()
        self.imprime_tablero()
        print()
        if self.gana(self.humano):
            print("El humano ha ganado!")
        elif self.gana(self.ia):
            print("La IA gana!")
        else:
            print("GATOOOOO!")

    def run(self):

        self.humano_elige()
        turno = random.choice([self.humano, self.ia])
        while not self.fin_de_juego:
            self.imprime_tablero()
            if turno == self.humano:
                self.juega_humano()
                if self.gana(self.humano):
                    self.fin_de_juego = True
                turno = self.ia
            else:
                self.juega_ia()
                if self.gana(self.ia):
                    self.fin_de_juego = True
                turno = self.humano
        self.imprime_resultado()

gato = Gato()
gato.run()
