#DESAFIO 1a INTRODUCCION A PYTHON
import math

#ingreso de datos
g = float(input("Ingrese el valor de la constante g: ")) #9.8
r_km = float(input("Ingrese el radio en Km: ")) #6371

#radio de km a metros
r_m = r_km * 1000

Ve = math.sqrt(2 * g * r_m)
print(f"La velocidad de escape es:", round(Ve,1), "m/s") #11174.6
