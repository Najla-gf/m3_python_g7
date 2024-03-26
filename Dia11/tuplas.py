"""
TUPLAS: 

Son inmutables, no se pueden modificar

Conjunto de datos ordenados e inmutables
se escriben en paréntesis ()

"""
tupla1= (1,3,5,7,9)
print(tupla1)
print(type(tupla1)) #<class 'tuple'> 

#se puede asignar una tupla a variables distintas y trabajarlas de manera individual
tupla2 = ("nombre", "Najla")
nom,texto = tupla2
print(nom) #nombre
print(texto) #Najla
#se puede consultar por posiciones al igual que en las listas
print(tupla2[0]) #se imprime nombre
print(tupla2[1]) #Najla
#print(tupla2[2]) #tuple index out of range

#INMUTABLES: no se le puede asignar ni modificar un dato
#tupla2[1] = "hola" #TypeError: 'tuple' object does not support item assignment
#tupla2[2] = "hola" #TypeError: 'tuple' object does not support item assignment

#ITERAR UNA TUPLA
for num in tupla1:
    print(num)


#para transformar un dicc a lista se debe usar el método LIST
list_dicc1 = list({"nota1":5,"nota2":6}.items()) #con items solo se recorre el listado del dicc 
print(list_dicc1) #dict_items([('nota1', 5), ('nota2', 6)])
print(list_dicc1[0]) #('nota1', 5)
print(list_dicc1[1]) #('nota2', 6)
print("")




