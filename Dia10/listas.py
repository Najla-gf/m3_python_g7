"""
LISTAS: 

() párentesis, se usa para las tuplas
{} llaves, se usa en diccionarios
[] corchetes, se usa en listas

Las listas son contenedores de datos, son mutables.
estructura: variable = [1, 2, 3, 4] <-- elementos de la lista es todo lo que está dentro de los corchetes separados por comas
las listas son conjunto de datos, separados por coma, ordenados según su ingreso.
La primera posición (INDICE) es cero

"""

lista_pares= [2,4,6,8,10,13]
#tamaño de la lista: 5 elementos
print(len(lista_pares)) #imprime el tamaño de la lista

print(lista_pares)#imprime los corchetes [2, 4, 6, 8, 10]
#indice o posición
print(lista_pares[0]) #imprime solo el numero 2
print(lista_pares[1]) #4
print(lista_pares[2]) #6
print(lista_pares[3]) #8
print(lista_pares[4]) #10
#print(lista_pares[5]) #IndexError pq no hay nada en la posicion 5
print("")
print(lista_pares[-1]) #10 muestra el ultimo elemento de la lista
print(lista_pares[-2]) #8 muestra el penultimo elemento de la lista
#Python nos deja utilizar elementos negativos

lista_vacia= []
#tamaño de la lista: 0 elementos (es incorrecto decir nulo o vacío)

#********METODOS*********
print(lista_pares.__dir__) #<built-in method __dir__ of list object at 0x0000022DDC76D900>
print(lista_pares.__dir__()) #['__new__', '__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', 
#'__iter__', '__init__', '__len__', '__getitem__', '__setitem__', '__delitem__', '__add__', '__mul__', '__rmul__', '__contains__', '__iadd__', '__imul__', 
#'__reversed__', '__sizeof__', 'clear', 'copy', 'append', 'insert', 'extend', 'pop', 'remove', 'index', 'count', 'reverse', 'sort', '__class_getitem__', 
#'__doc__', '__str__', '__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', 
#'__dir__', '__class__'] <<<--- se llaman built-in que permiten ver comportamientos de las listas
# muestra todas las funciones que tenemos disponibles para aplicar
print("")
#append(dato) ---> agrega un elemento al final de la lista
lista_vacia.append("Lunes") #se recomienda agregar info de a un elemento
print(lista_vacia)
lista_vacia.append("Martes")
lista_vacia.append("Miércoles")
print(lista_vacia)

#Insert(indice,elemento)
lista_vacia.insert(3,"Jueves") #['Lunes', 'Martes', 'Miércoles', 'Jueves']
lista_vacia.insert(3,"Viernes") #['Lunes', 'Martes', 'Miércoles', 'Viernes', 'Jueves'] 
print(lista_vacia) #Desplaza hacia la derecha todos los elementos de la posición en adelante, NO reemplaza el elemento
lista_vacia[3]="Jueves" #reemplazar el elemento en esa posición
print(lista_vacia) #['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Jueves'] 
lista_vacia.insert(10,"Sábado")
print(lista_vacia) #['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Jueves', 'Sábado'] Lo agrega al final

#En Javascrip se agrega el elemento en el orden que le digamos y deja los espacios vacios, en Python no, solo agrega al final
"""var lista = ['Lunes', 'Martes', 'Miercoles']
lista[10] = 'Domingo'
'Domingo'
lista
(11) ['Lunes', 'Martes', 'Miercoles', empty x 7, 'Domingo']"""

#POP() ---> saca el ultimo elemento dentro de la lista, se puede eliminar según la posición del index
lista_vacia.pop()
print(lista_vacia) #['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Jueves'] 
lista_vacia.pop(4)
print(lista_vacia) #['Lunes', 'Martes', 'Miércoles', 'Jueves']
lista_vacia.pop(-1)
print(lista_vacia) #elimina el ultimo elemento ['Lunes', 'Martes', 'Miércoles']
lista_vacia.pop(0)
print(lista_vacia) #['Martes', 'Miércoles']


lista_eliminados = []
lista_eliminados.append(lista_vacia.pop(0))
print(lista_eliminados) #Martes

colores = ['rojo', 'rosa']
colores.remove("rojo")
print(colores)

lista_vacia.append("Lunes")
lista_vacia.append("Martes")
lista_vacia.append("Miercoles")
lista_vacia.append("Jueves")
print(lista_vacia) #['Miércoles', 'Lunes', 'Martes', 'Miercoles', 'Jueves']

#REMOVE --- elimina un elemento de la lista
lista_vacia.remove("Miércoles") #['Lunes', 'Martes', 'Miercoles', 'Jueves']
print(lista_vacia) #se elimina el primer elemento repetido de izq a derecha

#REVERSE() ---> invierte los elementos de la lista y el cambio es PERMANENTE
lista_vacia.reverse()
print(lista_vacia) #['Jueves', 'Miercoles', 'Martes', 'Lunes']

#SORT(0) ----> ordena los elementos de manera ascendente por orden alfabético y permanente
lista_vacia.sort()
print(lista_vacia) #['Jueves', 'Lunes', 'Martes', 'Miercoles']

lista_pares.sort()
print(lista_pares)#[2, 4, 6, 8, 10, 13]


#ESTO NO ES UN RESPALDO DE DATOS
lista1 = lista_pares #se creó una nueva variable que apunta al mismo espacio de memoria


#RESPALDO DE LISTA (5 formas)
lista2 = lista_pares.copy() #respaldo de la lista original
lista3 = lista_pares[:] #respaldo de la lista original
lista4 = lista_pares + [] #respaldo de la lista original, concatenacion
lista5 = lista_pares * 1 #respaldo de la lista original, multiplicacion
lista6 = list(lista_pares) #respaldo de la lista original

lista_pares.pop()
print("Lista de pares", lista_pares) #Lista de pares [2, 4, 6, 8, 10]
print(lista1) #[2, 4, 6, 8, 10]
print(lista2) #[2, 4, 6, 8, 10, 13]
print(lista3) #[2, 4, 6, 8, 10, 13]
print(lista4)
print(lista5)
print(lista6)
print("")

#SORTED(lista, reverse=True) ---> ordena descendentemente y no es permanente
sorted(lista_pares, reverse=True) #ordena desc
sorted(lista_pares)#ordena asc
sorted(lista_pares, reverse= False)#ordena asc

print(sorted(lista_pares, reverse=True)) #[10, 8, 6, 4, 2]
print(lista_pares) #[2, 4, 6, 8, 10]
print("")

#INDEX(elemento) ----> entrega el inidice del elemento que se busca en una lista
print("Indice del elemento 8 es: ", lista_pares.index(8)) #3

lista_final = lista_pares + lista_vacia
print("Lista final", lista_final) #Lista final [2, 4, 6, 8, 10, 'Jueves', 'Lunes', 'Martes', 'Miercoles']




