#Proyecto integrador parte 3
#Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:
#Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.
#La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.
#Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os

import os

def borrar_terminal():
    """Borra la terminal según el sistema operativo."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    """Función principal del programa."""
    contador = 0
    tecla_presionada = ''

    while contador <= 50:  # Bucle hasta llegar a 50
        # Borrar la terminal
        borrar_terminal()

        # Imprimir el contador
        print(f"Contador: {contador}")

        # Incrementar el contador
        contador += 1

        # Leer la tecla presionada
        mensaje = "Presiona 'n' para continuar o 'q' para salir: "
        tecla_presionada = input(mensaje)

        # Salir del bucle si se presiona 'q'
        if tecla_presionada == 'q':
            break

if __name__ == "__main__":
    main()