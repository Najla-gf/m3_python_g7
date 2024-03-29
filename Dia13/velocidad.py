#Desafío - Estructuras de datos y funciones (II)
#Alertas telemáticas


def calculo_promedio(velocidades):
    suma = sum(velocidades) 
    promedio = suma / len(velocidades) #suma de las velocidades divididas por el total (len) de estas
    return promedio #13.2

def correas_sobre_promedio(velocidades):
    promedio = calculo_promedio(velocidades)
    correas_sobre_promedio = []
    for i, velocidad in enumerate(velocidades): #revisar el indice de cada velocidad de la lista
        if velocidad > promedio:
            correas_sobre_promedio.append(i)
    return correas_sobre_promedio #retorna las posiciones de la velocidades filtradas mayores al promedio

velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

promedio = calculo_promedio(velocidad)
print("El promedio de todas las velocidades es de:", promedio)

correas_sobre_promedio = correas_sobre_promedio(velocidad)
print("Las posiciones de las correas transportadoras mayores al promedio son:", correas_sobre_promedio)


