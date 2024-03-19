"""
Grupo1:
Jimena Traipe
Felipe Arias
Lollet Llanquinao
Najla Gatica
"""
#CHACHIPUN

import random

#Usuario ingresa opción
opcion_usuario = input("Ingresa 'piedra', 'papel' o 'tijera': \n").lower()

#Computador ingresa opción
opciones = ['piedra', 'papel', 'tijera'] #los corchetes crean una lista de las opciones válidas
opcion_computador = random.choice(opciones)

#Validar la opción del usuario y determinar el resultado del juego
if opcion_usuario in opciones: #el "in" sirve para validar que ingrese la opcion del usuario como válida
    print("Jugaste", opcion_usuario) #la coma separa los strings
    print("Computador jugó", opcion_computador)

    if opcion_usuario == opcion_computador: #todo este bloque va dentro del primer IF
        print("¡Empate!")
    #ingresar combinaciones validas con un AND para incluir ambas opciones sin importar el orden
    elif (opcion_usuario == 'piedra' and opcion_computador == 'tijera') or \
        (opcion_usuario == 'tijera' and opcion_computador == 'papel') or \
        (opcion_usuario == 'papel' and opcion_computador == 'piedra'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

else: #en caso de ingresar una opción diferente a las válidas
    print("Opción inválida: Debe ser piedra, papel o tijera.")