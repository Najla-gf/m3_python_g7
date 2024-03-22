"""
CICLO FOR 
for naviable in iterable

"""
#CICLO ES UN PROCESO de acciones repetitivas
#un conjunto de codigo se llaman sentencias
#que el iterable parta desde el 0 (por defecto) al 9.
#el valor que agregamos dentro NO será considerado
for i in range(10):
    print(i)


#opción 2: Se le aplica un rango de inicio desde el 4 hasta el 9
#siempre se trabaja con valores enteros
for i in range(4,10):
    print(i)


#opción 3 con 3 numeros dentro del rango, le especificamos el incremento
#En este caso quedaría: 4, 6, 8
for i in range(4,10,2):
    print(i)

    """
    FOR en JAVASCRIPT:
    
    for (let index = 4; index < 10; index++) {
    console.log(index);
}
        """
print("")
#Lista
numeros=[2,"4",True,3,"5"]
for numero in numeros: #La variable debe ir en SINGULAR
    print(numero)

print("")
#String -> son similares a las listas
texto = "Hola Mundo"
for caracter in texto:
    print(caracter)
print("")

#Diccionario, se componen de elementos contitutidos por una clave y valor
#(clave:valor)
datos_personales={
    "Nombre": "Najla",
    "Apellido": "Gatica",
    "Edad": 31,
}
for clave in datos_personales:
    print(clave) #imprime solo la clave

print("")

for clave in datos_personales:
    print(datos_personales[clave]) #imprime los valores

print("")

for clave,valor in datos_personales.items():
    print(f"clave: {clave} - valor: {valor}") #imprime ambas opciones

print("")

for par in datos_personales.items():
    print(par)

##otras formar de acceder a la clave y valor
for clave in datos_personales.keys():
    print(clave)

for valor in datos_personales.values():
    print(valor)


##ENUMERATE se utiliza para saber en qué posición se encuentra el elemento del iterable que estamos buscando
for posicion, caracter in enumerate(texto):
    print(f"La posición {posicion} del caracter {caracter}")

print("")

for posicion, numero in enumerate(numeros):
    print(f"La posición {posicion} del caracter {numero}")

print("")

#ZIP permite procesar varios iterables mientras la cantidad sea igual para todos
prefijo = ['La','El','La','El'] #Si le agrego otro artículo, no se muestra en la impresión
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')

print("")
#BREAK detiene el ciclo del codigo
numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]
for numero in numeros:
    print(numero)
    if numero ==3:
        break

print("fuera del for")




