#Archivo principal

#Aquí invocamos las funciones que creamos en scripts aparte
from masa import tipo_masa
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import quitar_ingrediente
from show import mostrar_ingredientes
from tiempo import estimar_tiempo
import datos as d
import time
import os
import sys
clear = "cls" if sys.platform == "win32" else "clear"

#Diccionario para diferenciar la masa, salsa y la lista de ingredientes
ingredientes_orden = d.ingredientes

#Se define el menú infito para que se muestre siempre:
print('¡Gracias por preferirnos!')
while True:
    os.system(clear) #Con esto vamos limpiando la terminar con cada menu
    opcion = input(d.menu) 

#Mientras tanto se definen todas las funciones en modulos aparte
#luego de generar todos los scripts, volvemos al archivo principal para invocarlos

#1. Cambiar masa:
    if opcion == '1':
        os.system(clear)
        eleccion = input(d.T_MASA).upper()
        ingredientes_orden = tipo_masa(ingredientes_orden, eleccion)
        print("") #agregamos un salto de linea

#2. Cambiar salsa:
    elif opcion == '2':
        os.system(clear)
        eleccion = input(d.T_SALSA).upper()
        ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion)
        print("")

#3. Agregar ingrediente:
    elif opcion == '3':
        os.system(clear)
        eleccion = int(input(d.AG_INGREDIENTE))
        ingredientes_orden = agregar_ingrediente(ingredientes_orden,eleccion)
        print("")

#4. Eliminar ingrediente:
    elif opcion == '4':
        os.system(clear)
        eleccion = int(input(d.QT_INGREDIENTE))
        ingredientes_orden = quitar_ingrediente(ingredientes_orden,
        eleccion)
        print("")

#5. Hacer la orden:
    elif opcion == '5':
        os.system(clear)
        tiempo = estimar_tiempo(ingredientes_orden)
        print(f'Su Pizza estará lista en {tiempo} minutos')
        ordenar = input('Desea ordenar ahora S/N: ').upper()
        print("")
        
        if ordenar == 'S':
            print('Gracias por ordenar en Pizza JAT')
            print('Disfrute su Pizza')
            time.sleep(3) #Los mensajes de finalización se mantienen 3 seg.
            exit()

#0. Mostrar ingredientes
    elif opcion == '0':
        os.system(clear)
        mostrar_ingredientes(ingredientes_orden)
        time.sleep(3)
        print("")

#Cancelar el pedido
    else:
        os.system(clear)
        print('Su pedido ha sido cancelado. Gracias por contactarse a Pizza JAT')
        time.sleep(3)
        exit()
