#Desafío - Estructuras de datos y funciones (II)
#Apoyo matemático.

def factorial(numero):
    if numero == 0: #si se ingresa un 0, asegurarse que se cambie a 1 para que no ocasione problemas
        return 1
    else:
        return numero * factorial(numero-1) #el factorial multiplica el numero por su anterior

def productoria(lista): #multiplica todos los elementos de una lista
    result = 1 #debe tener un valor iniciar para funcionar bien
    for num in lista:
        result *= num #multiplica por cada numero dela lista
    return result

#utilizando kwargs:
def calcular(**kwargs):
    for clave, valor in kwargs.items():
        #if clave == "factorial": esto funcionaria en caso de haber un solo factorial
        if clave.startswith("fact"): #cualquier argumento que comience con fact la detecta como factorial
            print("El factorial de", valor, "es:", factorial(valor))
        elif clave == "productoria":
            print("La productoria de", valor, "es:", productoria(valor))

#Invoca la función
calcular(factorial=5, productoria=[3,6,4,2,8], factorial_2=6)


#otra forma mediante funciones
"""def calcular(factorial_1, productoria_1, factorial_2):
    print("El factorial de", factorial_1, "es:", factorial(factorial_1))
    print("La productoria de", productoria_1, "es:", productoria(productoria_1))
    print("El factorial de", factorial_2, "es:", factorial(factorial_2))

calcular(factorial_1=5, productoria_1=[3,6,4,2,8], factorial_2=6)"""

