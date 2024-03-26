"""
SETS
Conjunto de datos que no permite duplicados
No es ordenado, siempre da resultados distintos al imprimir
se escriben con {}


"""


muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

print(muchos_animales)
#{'Tortuga', 'Hurón', 'Perro', 'Erizo de Tierra', 'Gato', 'Hamster'}

muchos_animales.add("Chancho")
print(muchos_animales)
#{'Chancho', 'Tortuga', 'Gato', 'Perro', 'Erizo de Tierra', 'Hamster', 'Hurón'}

#No se puede acceder a los datos de un set porque no se puede localizar el dato, es invocable.
#Pero SÍ se puede eliminar un dato del set que si exista
muchos_animales.remove("Perro")
print(muchos_animales)
#{'Gato', 'Hamster', 'Chancho', 'Tortuga', 'Hurón', 'Erizo de Tierra'}
#muchos_animales.remove("Leon")
#print(muchos_animales) #KeyError: "Leon"

muchos_animales.discard("Leon")
print(muchos_animales) #El método discard elimina el dato si es que existe

muchos_animales.pop() #Elimina un elemento al azar
print(muchos_animales)
#{'Hamster', 'Chancho', 'Hurón', 'Tortuga', 'Erizo de Tierra'}  

muchos_animales.clear() #Elimina TODOS los elementos dentro del set
print(muchos_animales) #set()

#MÉTODOS a aplicar
print(muchos_animales.__dir__())
print("")
print(dir(muchos_animales))