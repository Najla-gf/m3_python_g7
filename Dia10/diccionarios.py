"""
DICCIONARIOS {}

nos sirve para almacena runa gran cantidad de información en un mismo lugar

estructura de datos de pares= clave:valor (palabra:definicion)
Para acceder a los elementos en los diccionario se hace a través de la CLAVE
las claves no se generan automáticamente y no hay un orden, a diferencia de las listas
las claves pueden ser string, numéricos (enteros) y booleanos.
Si la clave existe, se modifica su valor. Si no existe, se agrega el par clave:valor al diccionario

"""
from os import system #esto es para ir borrando la terminal

diccionario = {
    1:"uno", 
    "dos":2,
    3: ["a", "b", "c"], #lista dentro del diccionario
    "dicc": {"A":"A Mayúscula"},
}
print(diccionario)

#Diccionario vacio
notas = {}
print(len(notas)) #cero

notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
"FELIPE" : 2
}

print(len(notas)) #5
print(notas)

system("cls") #esto es para ir borrando la terminal

#Acceso a los elementos(valores)
print(notas["Camila"]) #7
print(notas["Antonio"]) #5
print(notas["Felipe"]) #6
print(notas["Daniela"]) #5
print(notas["Vicente"]) #7
print(notas["FELIPE"]) #2
#el texto debe ser IGUAL al de la clave
#LAS CLAVES DEBEN SER UNICAS
#Si se repite una clave, se sobreescribe el primer valor
#por ej: si hay 2 vicentes y el otro tiene nota 1, queda vicente: 1 como final.

print(notas)
#para definir un diccionario usamos llaves ({}),
#pero para acceder a sus elementos usamos corchetes [].
notas["Julio"] = 4 #se agrega una nueva clave y valor --> [clave] = valor
print(notas) #{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'FELIPE': 2, 'Julio': 4}

#Modificar par clave:valor
notas["Julio"] = 5
print(notas) #se sobreescribe, ahora tiene un 5

#Eliminar par clave:valor
del notas["FELIPE"]
print(notas) #{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'Julio': 5}

#Segunda forma de eliminar con pop() ---> al eliminar, capturamos el valor
eliminado = notas.pop("Camila") #notas["Camila"]
print("valor eliminado: ", eliminado) #7
print(notas) #{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'Julio': 5}
print("")

notas2= {
    "Daniel": 7,
    "Belen": 6,
}

"""notas.update(notas2)
print(notas) #{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'Julio': 5, 'Daniel': 7, 'Belen': 6}
#Se actualiza el primer diccionario de notas y se agregar los nuevos elementos al final de la lista
"""
notas2.update(notas)
print(notas2) #{'Daniel': 7, 'Belen': 6, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'Julio': 5}
#se une el segundo diccionario al primero, los datos de notas 2 quedan primero.
print("")
#COLISIONES: Cuando hay una clave en común, el valor del segundo diccionario sobreescribe al del primero.

print(notas2.keys())
#dict_keys(['Daniel', 'Belen', 'Antonio', 'Felipe', 'Daniela', 'Vicente', 'Julio'])
print(notas2.values())
#dict_values([7, 6, 5, 6, 5, 7, 5])
print(notas2.items()) #items entrega resultados en par de clave:valor, como tupla
#dict_items([('Daniel', 7), ('Belen', 6), ('Antonio', 5), ('Felipe', 6), ('Daniela', 5), ('Vicente', 7), ('Julio', 5)])
print("")

#get(clave) ---> entrega el valor asociado a la clave
print(notas2.get("Daniel")) #7
#al consultar por una clave inexistente retorna un none
print(notas2.get("Alexis")) #None -- NoneType: tipo de dato
#Se puede especificar el valor de retorno al no existir la clave
print(notas2.get("Alexis", "Valor no existe")) #Valor no existe

