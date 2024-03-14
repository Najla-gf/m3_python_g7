#DESAFIO 1b INTRODUCCION A PYTHON
#valores
p_normal = float(input("Ingrese el precio de la suscripción normal: "))
p_premium = 1.5 * p_normal
u_normal = int(input("Ingrese el número de usuarios normales: "))
u_premium = int(input("Ingrese el número de usuarios premium: "))
gt = float(input("Ingrese los gastos totales: "))

utilidades = (p_normal * u_normal + p_premium * u_premium) - gt

print("Las utilidades del proyecto son:", utilidades)
