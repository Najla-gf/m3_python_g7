#Desafío - Estructuras de datos y funciones (II)
#Actividad 1

import sys

def filtro_umbral(precios, umbral, mayor_que=True): #definimos la funcion y las variables que usaremos
    productos_filtrados = []
    for clave, valor in precios.items():
        if (mayor_que and valor > umbral) or (not mayor_que and valor < umbral):
            productos_filtrados.append(clave) #almacena los productos que cumplen la condicion
    return productos_filtrados

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

if len(sys.argv) == 2: #esto especifica la cantidad de argumentos que se ingresan a la terminal
    #siendo 1 el umbral y 2 si es mayor o menor
    umbral = int(sys.argv[1])
    productos_mayor_que = filtro_umbral(precios, umbral)
    print("Productos con precios mayores que", umbral, ":")
    print(", ".join(productos_mayor_que))

elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    mayor_que = sys.argv[2].lower() #posicion 2 seria si es mayor o menor
    if "mayor" not in mayor_que and "menor" not in mayor_que:
        print("Lo sentimos, no es una operación válida.")
        exit()
    mayor_que = mayor_que == "mayor"
    productos_filtrados = filtro_umbral(precios, umbral, mayor_que)
    if mayor_que:
        print("Productos con precios mayores que", umbral, ":")
    else:
        print("Productos con precios menores que", umbral, ":")
    print(", ".join(productos_filtrados))

"""else:
    print("Lo sentimos, no es una operación válida.")"""

