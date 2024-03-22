"""
Generar los los 10 primeros pares dentro de una lista
"""


n = 10

lista_pares = [] #estamos creando una lista vacía, tamaño 0 elementos
for i in range(n): #la i toma el valor de 0 y el ultimo es 9
    lista_pares.append(2*i + 2) #en el parentesis va lo que queremos guardar
#el append agrega elementos a la lista
#[formula for variable in range(n)]
lista_pares2 = [2*i + 2 for i in range(n)]

"""
for i in range(1,n+1): #
    lista_pares.append(2*i )#[2,4,6,8,10,12,14,16,18,20]
for i in range(2,(2*n+2),2): #
    lista_pares.append(i )#[2,4,6,8,10,12,14,16,18,20]
"""
print(lista_pares)
print(lista_pares2)
print([2*i + 2 for i in range(n)])

print("")

##[expresión1 if condición1 else expresión2 for variable in iterable]
valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
        
print(divisibles)

divisibles2 = ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in valores ]
print(divisibles2)

##FILTRAR

lista = ['Lechugas', 'Tomates', 5, 10,True, False, True, 'Papas',5.1, 45.2, 1, 2, 0]
lista_str= []
lista_int= []
count_str = 0
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
        lista_str.append(elemento)
    elif type(elemento) is int:
        lista_int.append(elemento)
        
print(count_str)
print(lista_str)
print(lista_int)

lst_str = [elemento for elemento in lista if type(elemento) is str ]
print(len(lst_str))
print(lst_str)

##DICIONARIO COMPREHENSION
claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
diccionario2 = {k:v for k,v in zip(claves, valores)} #el diccionario hace que se guarden o almacenen los datos
print(diccionario2) #aquí solo se imprime y muestra los datos



