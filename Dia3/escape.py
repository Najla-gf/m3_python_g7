#DESAFIO 1a INTRODUCCION A PYTHON
from math import sqrt #se recomienda importar SOLO lo que vamos a ocupar

#ingreso de datos
gravedad = float(input("Ingrese el valor de la constante g: ")) #9.8
radio_km = float(input("Ingrese el radio en Km: ")) #6371

#radio de km a metros
radio_m = radio_km * 1000

velocidad_escape = sqrt(2 * gravedad * radio_m)
print(f"La velocidad de escape es", round(velocidad_escape,1), "m/s") #11174.6
