import math

#Funciones
#Definimos la función para el promedio
def media(lista):
    return sum(lista)/len(lista)

#Funcion de desviacion estandar
#se calculan las diferencias al cuadrado entre cada elemento de la lista y la media (list comprehension)
#se saca la raíz cuadrada de la suma de estas diferencias dividida por el número de elementos menos 1.
def sdd(lista, media):
    diff = [(elemento-media) **2 for elemento in lista]
    return math.sqrt(sum(diff)/(len(lista)-1))

#la funcion resultado devuelve 3 resultados
def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estandarizada = [(valor-m)/sd for valor in lista]
    return m, sd, lista_estandarizada

lista = [1, 2, 3, 4, 5, 6]

m, desv_st, l_e = resultado(lista)
print(f"La media es {m}")
print(f"La desviación estándar es {desv_st}")
print(f"La lista estandarizada es {l_e}")