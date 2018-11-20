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
                [0,0,0],
                [0,0,0],
                [0,0,0]
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
        resp = input("Humano elige 'x' o 'o'? ")
        if resp.lower() == 'x':
            self.simbs = [".", "x", "o"]
        else:
            self.simbs = [".", "o", "x"]
        print()

    def tirada(self, p, jugador):
        self.tablero[p[0]][p[1]] = jugador

    def juega_humano(self):
        print()
        resp = input("Turno del humano, elige casilla (ren, col)? ")
        p = [int(v) for v in resp.split(",")]
        self.tirada(p, self.humano)
        print()

    def casillas_libres(self):
        return [(i, j) for j in random.sample(range(3), 3)
                for i in random.sample(range(3), 3)
                if self.tablero[i][j] == 0]

    def juega_ia(self):
        print()
        print("Turno de la IA!")
        casillas = self.casillas_libres()

        tablero_aux = [ren[:] for ren in self.tablero]
        for c in casillas:
            self.tirada(c, self.ia)
            if self.gana(self.ia):
                return
            else:
                self.tablero = [ren[:] for ren in tablero_aux]
        for c in casillas:
            self.tirada(c, self.humano)
            if self.gana(self.humano):
                self.tirada(c, self.ia)
                return
            else:
                self.tablero = [ren[:] for ren in tablero_aux]

        for c in casillas:
            if c[0] in [0, 2] and c[1] in [0, 2]:
                self.tirada(c, self.ia)
                return

        if (1, 1) in casillas:
            self.tirada((1, 1), self.ia)
            return

        self.tirada(casillas[0], self.ia)
        print()

    def gana(self, jugador):
        
        for ren in self.tablero:
            if sum(ren) == 3 * jugador:
                return True
        for col in zip(*self.tablero):
            if sum(col) == 3 * jugador:
                return True
        diag1 = [ren[i] for i, ren in enumerate(self.tablero)]
        if sum(diag1) == 3 * jugador:
            return True
        diag2 = [ren[2-i] for i, ren in enumerate(self.tablero)]
        if sum(diag2) == 3 * jugador:
            return True

        return False

    def imprime_resultado(self):
        print()
        self.imprime_tablero()
        print()
        if self.gana(self.humano):
            print("El humano gana!")
        elif self.gana(self.ia):
            print("La IA gana!")
        else:
            print("GATOOOOO!")
        print()

    def es_gato(self):
        return False if self.casillas_libres() else True

    def run(self):

        self.humano_elige()
        turno = random.choice([self.humano, self.ia])
        while not self.fin_de_juego and not self.es_gato():
            self.imprime_tablero()
            if turno == self.humano:
                self.juega_humano()
                if self.gana(self.humano):
                    self.fin_de_juego = True
                else:
                    turno = self.ia
            else:
                self.juega_ia()
                if self.gana(self.ia):
                    self.fin_de_juego = True
                else:
                    turno = self.humano
        self.imprime_resultado()


gato = Gato()
gato.run()
