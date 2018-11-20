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

import copy
import random


class Tablero():
    """
    Clase para representar un tablero
    """
    def __init__(self):
        """
        Inicializa el tablero
        """
        self.tablero = [
            [0, 0 ,0],
            [0, 0 ,0],
            [0, 0 ,0]
        ]

    def casillas_libres(self):
        """
        Regresa una lista con todas las casillas libres
        """
        return [(i, j) for j in random.sample(range(3), 3)
                for i in random.sample(range(3), 3)
                if self.es_vacia((i, j))]

    def es_empate(self):
        """
        Regreso True si hay empate, False en caso contrario
        """
        return False if self.casillas_libres() else True

    def gana(self, jugador):
        """
        Regresa True si jugador gana, False en caso contrario
        """
        # Se busca en horizontales
        for ren in self.tablero:
            if abs(sum(ren)) == 3 and jugador in ren:
                return True
        # Se busca en verticales
        for col in zip(*self.tablero):
            if abs(sum(col)) == 3 and jugador in col:
                return True
        # Se busca en diagonales
        diag1 = [self.tablero[i][i] for i in range(3)]
        if abs(sum(diag1)) == 3 and jugador in diag1:
            return True
        diag2 = [self.tablero[2-i][i] for i in range(3)]
        if abs(sum(diag2)) == 3 and jugador in diag2:
            return True

        return False

    def humano_elije(self, simb):
        """
        Asigna los símbolos en base a la elección del humano
        """
        if simb == "x":
            self.simbolos = [".", "x", "o"]
        else:
            self.simbolos = [".", "o", "x"]

    def imprime(self):
        """
        Imprime el tablero
        """
        print()
        print("-"*10)
        print("  0 1 2")
        for i, linea in enumerate(self.tablero):
            print("{} {} {} {}".format(
                str(i), *[self.simbolos[v] for v in linea]))
        print("-"*10)

    def haz_tirada(self, p, j):
        """
        Realiza una tirada en la casilla p en el tablero del jugador j
        """
        self.tablero[p[0]][p[1]] = j

    def es_vacia(self, p):
        """
        Regresa True si la casilla en p está vacía, False de lo contrario
        """
        return True if self.tablero[p[0]][p[1]] == 0 else False

    def es_esquina(self, p):
        """
        Regresa True si la casilla está en una esquina, False de lo
        contrario
        """
        return True if p[0] in [0, 2] and p[1] in [0, 2] else False

    def juega_humano(self):
        """
        Solicita la siguiente tirada del humano y actualiza el tablero
        """
        print("Es tu turno humano!")
        tirada = False
        while not tirada:
            resp = input("Elije una casilla (ren, col)? ")
            p = [int(v) for v in resp.split(",")]
            if self.es_vacia(p):
                self.haz_tirada(p, 1)
                tirada = True
            else:
                print("Casilla ocupada, elije otra!")
                print()

    def juega_ia(self):
        """
        Realiza la siguiente tirada de la IA y actualiza tablero
        """
        print("Turno de la IA!")

        # Se buscan las casillas disponibles de forma aleatoria
        casillas = self.casillas_libres() 
        # Se busca si la IA puede ganar en la siguiente tirada
        for c in casillas:
            tablero2 = copy.deepcopy(self)
            tablero2.haz_tirada(c, -1)
            if tablero2.gana(-1):
                self.haz_tirada(c, -1)
                return

        # Se busca si el Humano puede ganar en la siguiente tirada, si
        # es así hay que bloquearlo
        for c in casillas:
            tablero2 = copy.deepcopy(self)
            tablero2.haz_tirada(c, 1)
            if tablero2.gana(1):
                self.haz_tirada(c, -1)
                return

        # Ahora la estrategía es tirar en el esquinas, centro o lados,
        # en ese orden.
        esquinas = [c for c in casillas if self.es_esquina(c)]
        if esquinas:
            self.haz_tirada(esquinas[0], -1)
            return

        casillas = [c for c in casillas if c not in esquinas]
        if (1, 1) in casillas:
            self.haz_tirada((1, 1), -1)
            return

        casillas = [c for c in casillas if c is not (1, 1)]
        if casillas:
            seld.haz_tirada(casillas[0], -1)
            return

class Gato():
    """
    Clase para el juego del gato
    """
    def __init__(self):
        """
        Constructor de la clase
        """
        self.nuevo_juego()

    def nuevo_juego(self):
        """
        Inicializa las condiciones para un nuevo juego
        """
        self.termina_juego = False  # Por default el juego no ha terminado
        self.mensaje_inicial()
        self.tablero = Tablero()
        self.humano_elige_simbolo()

    def mensaje_inicial(self):
        """
        Imprime un mensaje inicial del juego
        """
        print("""

        Juego de gato
        -------------

        """)

    def humano_elige_simbolo(self):
        """
        Muestra mensaje para que humano elija el símbolo a usar
        """
        simb = None
        while not simb:
            resp = input("Humano quieres jugar con 'x' o 'o' ? ")
            if resp.lower() == "x" or resp.lower() == "o":
                simb = resp.lower()
            else:
                print("Elección incorrecta, intenta de nuevo!\n")
        self.tablero.humano_elije(simb)

    def imprime_resultado(self, turno):
        """
        Imprime el resultado del ganador o empate)
        """

        self.tablero.imprime()

        if self.tablero.gana(turno):
            print("""

            El ganador es {}

            """.format("el Humano" if turno == 1 else "la IA"))
        else:
            print("""

            El juego es un empate!

            """)

    def otro_juego(self):
        """
        Pregunta al humano si desea realizar otro juego
        """
        print()
        valida = False
        while not valida:
            resp = input("Desea realizar otro juego? (Si/No)")
            if resp.lower() in ["si", "s", "no", "n"]:
                valida = True
                resp = resp.lower()
            else:
                print("Respuesta incorrecta, intente de nuevo!\n")
        if resp in ["si", "s"]:
            self.nuevo_juego()
        else:
            self.termina_juego = True

    def run(self):
        """
        Ejecuta del ciclo principal del juego
        """

        while not self.termina_juego:
            turno = random.choice([-1, 1])  # Se elige quien inicia el juego al azar
            while not self.tablero.es_empate() and not self.tablero.gana(turno):
                self.tablero.imprime()
                if turno == 1:
                    self.tablero.juega_humano()
                    if self.tablero.gana(turno):
                        continue
                    turno = -1
                else:
                    self.tablero.juega_ia()
                    if self.tablero.gana(turno):
                        continue
                    turno = 1
            self.imprime_resultado(turno)
            self.otro_juego()


# Se crea una instancia del juego
gato = Gato()

# Se inicia el juego
gato.run()
