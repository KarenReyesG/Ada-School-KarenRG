# Proyecto integrador parte 2
# El proyecto del curso consistirá en implementar un juego de recorrer laberintos, estará basado enteramente en la terminal y trabajaremos con caracteres ASCII.

# Para esta primera parte debemos aprender a usar la librería `readchar` que nos permitirá leer un caracter suelto del teclado.
#Tu tarea es
# Instalar la librería: https://pypi.org/project/readchar/
# Investigar cómo leer un caracter del teclado
# Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP


from readchar import readkey, key
# Pedir el nombre jugador:
name = input("Su nombre es?")

# Saludar al jugador:
print ("Bienvenido al juego del laberito", name)

# Iniciar el juego del laberinto

trigger = True

while trigger:
    print("Presiona una tecla para continuar. Para salir, presiona la flecha arriba (↑)")    
    tecla = readkey()
    
    print(f'La tecla presionada es la {tecla}')

    if tecla == key.UP:
        print("Saliendo")

        trigger = False