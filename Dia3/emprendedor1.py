#DESAFIO 1b INTRODUCCION A PYTHON

# datos 
# se recomienda siempre trabajar con FLOAT cuando hablamos de valores o precios
precio = float(input("Ingrese el precio de suscripción en CLP: "))
usuarios = int(input("Ingrese el número de usuarios: "))
gastos_totales = float(input("Ingrese los gastos totales en CLP: "))

#ecuacion
utilidades = precio * usuarios - gastos_totales

print(f"Las utilidades del proyecto son: {utilidades} CLP")
