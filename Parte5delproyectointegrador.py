# Proyecto integrador Parte 5

import os
import random
from typing import List, Tuple
import readchar
from readchar import readkey, key

class Juego:
    def __init__(self, mapa, p_i, p_f):
        self.mapa = mapa
        self.p_i = p_i
        self.p_f = p_f

    def matriz_carac(self, mapa: str):
        filas = mapa.split("\n")
        matriz_map = [list(indi) for indi in filas]
        return matriz_map

    def limpiar(self, matriz_map: list):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system("cls")
        for fil in matriz_map:
            print(" ".join(fil))

    def main_loop(self, mapa_lab: List[List[str]], p_i: Tuple[int, int], p_f: Tuple[int, int]):
        px, py = self.p_i
        personaje = "P"
        mapa_lab[px][py] = personaje
        self.limpiar(mapa_lab)
        while (px, py) != self.p_f:
            mapa_lab[px][py] = personaje
            posicion = readchar.readkey()
            px_new, py_new = px, py
            if posicion == key.UP:
                px_new -= 1
            elif posicion == key.DOWN:
                px_new += 1
            elif posicion == key.LEFT:
                py_new -= 1
            elif posicion == key.RIGHT:
                py_new += 1
            else:
                print("Unicamente puedes usar las flechas :/")

            num_filas = len(mapa_lab)-1
            num_columnas = len(mapa_lab)-1

            if 0 <= px_new and num_filas >= px_new and 0 <= py_new and num_columnas >= py_new and mapa_lab[px_new][py_new] != "#":
                mapa_lab[px][py] = "."
                px, py = px_new, py_new
            else:
                print("Has topado con una pared o estás en el límite del laberinto :(")
            self.limpiar(mapa_lab)
        print("¡Felicidades!")

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        archivos = os.listdir(path_a_mapas)
        archivo_elegido = random.choice(archivos)
        path_completo = f"{path_a_mapas}/{archivo_elegido}"
        with open(path_completo, "r") as archivo:
            contenido = archivo.read()
            contenido = contenido.strip()
            filas = contenido.split("\n")
            self.mapa = contenido
            self.p_i = tuple(map(int, filas.split()))
            self.p_f = tuple(map(int, filas.split()))
            self.mapa = "\n".join(filas[2:])

    def leer_archivo(self, path_a_mapas):
        archivos = os.listdir(path_a_mapas)
        archivo_elegido = random.choice(archivos)
        path_completo = f"{path_a_mapas}/{archivo_elegido}"
        with open(path_completo, "r") as archivo:
            contenido = archivo.read()
            contenido = contenido.strip()
            return contenido

# Programa principal
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Convierte el mapa de cadena a matriz de caracteres
mapa_matriz = [list(fila) for fila in laberinto.split("\n")]

# Define las coordenadas del inicio y fin
posicion_inicial = (0, 0)
posicion_final = (len(mapa_matriz) - 1, len(mapa_matriz) - 1)

# Inicia el main loop
juego = Juego(laberinto, posicion_inicial, posicion_final)
juego.main_loop(mapa_matriz, posicion_inicial, posicion_final)


class Game:
    def __init__(self, laberinto, initialPoint, name):
        self.laberinto = laberinto
        self.initialPoint = initialPoint
        self.name = name
        self.trigger = True

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')  #Borrar la consola


    def string_to_caracters_matrix(self, string: str):
        """
            Esta funcion convierte un string en una matriz de caracteres
        """
        return [list(line) for line in string.split("\n")]

    def clearAndShowMatrix(self, matrix):
        """
            Esta funcion limpia la consola y muestra la matriz
        """
        self.clear()
        for line in matrix:
            print("".join(line))

    def goDown(self,currentPoint):
        currentPoint[0] = currentPoint[0] + 1
        return currentPoint

    def goUP(self, currentPoint):
        currentPoint[0] = currentPoint[0] - 1
        return currentPoint

    def goLEFT(self, currentPoint):
        currentPoint[1] = currentPoint[1] - 1
        return currentPoint

    def goRIGHT(self, currentPoint):
        currentPoint[1] = currentPoint[1] + 1
        return currentPoint

    def mainLoop(self, map, initialPoint, finalPoint):
        trigger = self.trigger
        currentPoint = list(initialPoint)
        while trigger:
            map[currentPoint[0]][currentPoint[1]] = "P"
            self.clearAndShowMatrix(map)
            previousPoint = currentPoint
            map[previousPoint[0]][previousPoint[1]] = "."
            print(currentPoint, finalPoint)
            key_ = readkey()
            if key_ == key.UP:
                if (map[currentPoint[0] - 1][currentPoint[1]] != "#"): #Verificamos que no haya una pared
                    currentPoint = self.goUP(currentPoint)
            elif key_ == key.DOWN:
                if map[currentPoint[0] + 1][currentPoint[1]] != "#":
                    currentPoint = self.goDown(currentPoint)
            elif key_ == key.LEFT:
                if map[currentPoint[0]][currentPoint[1] - 1] != "#":
                    currentPoint = self.goLEFT(currentPoint)
            elif key_ == key.RIGHT:
                if map[currentPoint[0]][currentPoint[1] + 1] != "#":
                    currentPoint = self.goRIGHT(currentPoint)
            else:
                trigger = False
            if tuple(currentPoint) == finalPoint:
                trigger = False
                print(f"{self.name}, Ganaste!")

    def start(self):
        map = self.string_to_caracters_matrix(self.laberinto)
        #Punto Final
        Pf = (len(map) - 1, len(map[0])-2)
        self.mainLoop(map, self.initialPoint, Pf)

class GameArchivo():
    def __init__(self, name):
        self.name = name
    def leer_archivos_txt(self):
        path_carpeta = "laberintos"
        archivos = os.listdir(path_carpeta)
        archivo = random.choice(archivos)


        mapa = """"""
        with open(f"{path_carpeta}/{archivo}") as archivo:
            mapa += archivo.read()

        return mapa
    def init(self):
        laberinto = self.leer_archivos_txt()
        P0 = (0,0)
        self.game = Game(laberinto, P0, self.name)
        #ejecutamos el juego
        self.game.start()
