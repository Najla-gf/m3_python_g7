#DESAFIO 1b INTRODUCCION A PYTHON
#valores
precio = float(input("Ingrese el precio de suscripción en CLP: "))
usuarios = int(input("Ingrese el número de usuarios: "))
gastos_totales = float(input("Ingrese los gastos totales en CLP: "))
utilidad_anterior = float(input("Ingrese las utilidades del año anterior: "))

#Utilidades actuales formula
utilidades_actuales = precio * usuarios - gastos_totales

#ecuacion razon
razon_utilidades = utilidades_actuales / utilidad_anterior

print(f"Las utilidades del proyecto son {utilidades_actuales} CLP")
print(f"La razón entre las utilidades actuales y del año anterior es: {round(razon_utilidades, 2)}")
