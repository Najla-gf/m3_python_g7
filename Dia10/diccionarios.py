"""
DICCIONARIOS {}

estructura de datos de pares= clave:valor (palabra:definicion)
Para acceder a los elementos en los diccionario se hace a través de la CLAVE
las claves no se generan automáticamente y no hay un orden, a diferencia de las listas
las claves pueden ser string, numéricos (enteros) y booleanos.


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
#el texto debe ser IGUAL al de la clave
#LAS CLAVES DEBEN SER UNICAS
#Si se repite una clave, se sobreescribe el primer valor
#por ej: si hay 2 vicentes y el otro tiene nota 1, queda vicente: 1 como final.



