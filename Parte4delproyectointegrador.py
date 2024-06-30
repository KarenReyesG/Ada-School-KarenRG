# Función para convertir el mapa de cadena a matriz de caracteres
def convertir_mapa_a_matriz(laberinto):
    # Utiliza la función split("\n") para separar el mapa por filas
    # y list() para convertir cada fila a una lista de caracteres
    mapa_matriz = [list(fila) for fila in laberinto.split("\n")]
    return mapa_matriz

# Función para limpiar la pantalla y mostrar la matriz
def mostrar_mapa(mapa_matriz):
    # Limpia la pantalla
    print("\n" * 50)
    # Muestra la matriz
    for fila in mapa_matriz:
        print("".join(fila))

# Función para el main loop
def main_loop(mapa_matriz, posicion_inicial, posicion_final):
    # Inicializa las coordenadas del jugador con la posición inicial
    px, py = posicion_inicial
    # Asigna el caracter P en el mapa a las coordenadas (px, py)
    mapa_matriz[px][py] = "P"
    
    # Procesa mientras (px, py) no coincida con la coordenada final
    while (px, py) != posicion_final:
        # Muestra el mapa
        mostrar_mapa(mapa_matriz)
        
        # Lee del teclado las teclas de flechas
        tecla = input("Ingrese una tecla de flecha (arriba, abajo, izquierda, derecha): ")
        
        # Verifica la tecla ingresada y actualiza la posición del jugador
        if tecla == "arriba":
            nueva_py = py
            nueva_px = px - 1
        elif tecla == "abajo":
            nueva_py = py
            nueva_px = px + 1
        elif tecla == "izquierda":
            nueva_py = py - 1
            nueva_px = px
        elif tecla == "derecha":
            nueva_py = py + 1
            nueva_px = px
        
        # Verifica si la nueva posición es válida
        if (0 <= nueva_px < len(mapa_matriz)) and (0 <= nueva_py < len(mapa_matriz)):
            if mapa_matriz[nueva_px][nueva_py] != "#":
                # Restaura la anterior posición a .
                mapa_matriz[px][py] = "."
                # Actualiza la posición del jugador
                px, py = nueva_px, nueva_py
                # Asigna el caracter P en el mapa a las coordenadas (px, py)
                mapa_matriz[px][py] = "P"
    
    # Muestra el mapa final
    mostrar_mapa(mapa_matriz)
    print("¡Has llegado al final!")

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
mapa_matriz = convertir_mapa_a_matriz(laberinto)

# Define las coordenadas del inicio y fin
posicion_inicial = (0, 0)
posicion_final = (len(mapa_matriz) - 1, len(mapa_matriz) - 1)

# Inicia el main loop
main_loop(mapa_matriz, posicion_inicial, posicion_final)