#DESAFIO 1b INTRODUCCION A PYTHON
#valores
p = float(input("Ingrese el precio de suscripción: "))
u = int(input("Ingrese el número de usuarios: "))
gt = float(input("Ingrese los gastos totales: "))
u_anterior = float(input("Ingrese las utilidades del año anterior: "))

#Utilidades actuales
u_actuales = p * u - gt

razon_utilidades = u_actuales / u_anterior

print("Las utilidades del proyecto son:", round(u_actuales, 2))
print("La razón entre las utilidades actuales y del año anterior es:", round(razon_utilidades, 2))
