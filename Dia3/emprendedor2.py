#DESAFIO 1b INTRODUCCION A PYTHON
#valores
precio_normal = float(input("Ingrese el precio de la suscripción normal en CLP: "))
precio_premium = 1.5 * precio_normal
usuario_normal = int(input("Ingrese el número de usuarios normales: "))
usuario_premium = int(input("Ingrese el número de usuarios premium: "))
gastos_totales = float(input("Ingrese los gastos totales en CLP: "))

utilidades = (precio_normal * usuario_normal + precio_premium * usuario_premium) - gastos_totales

print(f"Las utilidades del proyecto son: {utilidades} CLP")
