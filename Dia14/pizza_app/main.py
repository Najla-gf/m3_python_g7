#Archivo principal

#Aquí invocamos las funciones que creamos en scripts aparte
from masa import tipo_masa
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import quitar_ingrediente
from show import mostrar_ingredientes
from tiempo import estimar_tiempo


#Diccionario para diferenciar la masa, salsa y la lista de ingredientes
ingredientes_orden = {'masa': 'Masa Tradicional', 
                    'salsa': 'Salsa de Tomate', 
                    'ingredientes': ['Queso'] 
                    } 

#Se define el menú infito para que se muestre siempre:
print('¡Gracias por preferirnos!')
while True:
    opcion = opcion = input('''¿Qué desea realizar? 
                1. Cambiar tipo de Masa 
                2. Cambiar tipo de Salsa 
                3. Agregar Ingredientes 
                4. Eliminar Ingredientes 
                5. Ordenar con los Ingredientes Actuales 
                
                0. Consultar ingredientes de la pizza 
                
                Otro Número cancelará el pedido. 
                > ''') 

#Mientras tanto se definen todas las funciones en modulos aparte
#luego de generar todos los scripts, volvemos al archivo principal para invocarlos

#1. Cambiar masa:
    if opcion == '1':
        eleccion = input("""Escoja el tipo de Masa:
            T). Masa Tradicional
            D). Masa Delgada
            B). Masa con Bordes de Queso
            > """).upper()
        ingredientes_orden = tipo_masa(ingredientes_orden, eleccion)


#2. Cambiar salsa:
    elif opcion == '2':
        eleccion = input('''Seleccione su tipo de Salsa:
            T). Salsa de Tomate
            A). Salsa Alfredo
            B). Salsa Barbecue
            P). Salsa Pesto
            > ''').upper()
        ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion)


#3. Agregar ingrediente:
    elif opcion == '3':
        eleccion = int(input('''Seleccione su Ingrediente:
            1). Tomate
            2). Champiñones
            3). Aceituna
            4). Cebolla
            5). Pollo
            6). Jamón
            7). Carne
            8). Tocino
            9). Queso
            > '''))
        ingredientes_orden = agregar_ingrediente(ingredientes_orden,eleccion)


#4. Eliminar ingrediente:
    elif opcion == '4':
        eleccion = int(input('''Seleccione qué ingrediente quitar:
            1). Tomate
            2). Champiñones
            3). Aceituna
            4). Cebolla
            5). Pollo
            6). Jamón
            7). Carne
            8). Tocino
            9). Queso
            > '''))
        ingredientes_orden = quitar_ingrediente(ingredientes_orden,
        eleccion)


#5. Hacer la orden:
    elif opcion == '5':
        tiempo = estimar_tiempo(ingredientes_orden)
        print(f'Su Pizza estará lista en {tiempo} minutos')
        ordenar = input('Desea ordenar ahora S/N: ').upper()
    
        if ordenar == 'S':
            print('Gracias por ordenar en Pizza JAT')
            print('Disfrute su Pizza')
            exit()

#0. Mostrar ingredientes
    elif opcion == '0':
        mostrar_ingredientes(ingredientes_orden)

#Cancelar el pedido
    else:
        print('Su pedido ha sido cancelado. Gracias por contactarse a Pizza JAT')
        exit()
