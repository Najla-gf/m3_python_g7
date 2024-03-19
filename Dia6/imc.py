"""
Grupo1:
Jimena Traipe
Felipe Arias
Lollet Llanquinao
Najla Gatica
"""

#Le pedimos al usuario ingresar los datos
peso= float(input("Ingrese el peso en kg: "))
altura= float(input("Ingrese la altura en centimetros: "))

#pasar cm a mt, se divide por 100
altura_mt= altura/100
print(f"Su altura es {altura_mt} m")

#formula
indice_masa_corporal = peso/(altura_mt**2)
print(f"Su IMC es de {indice_masa_corporal:.2f}")

#Condiciones
#indice_masa_corporal=18 le asignamos un valor para probar las condiciones (comentamos lo de arriba)
if indice_masa_corporal < 18.5:
    print("La clasificación OMS es Bajo Peso")
elif indice_masa_corporal >=18.5 and indice_masa_corporal < 25:
    print("La clasificación OMS es Adecuado")
elif indice_masa_corporal >= 25 and indice_masa_corporal < 30:
    print("La clasificación OMS es Sobrepeso")
elif indice_masa_corporal >= 30 and indice_masa_corporal < 35:
    print("La clasificación OMS es Obesidad Grado I")
elif indice_masa_corporal >= 35 and indice_masa_corporal < 40:
    print("La clasificación OMS es Obesidad Grado II")
elif indice_masa_corporal >=40:
    print("La clasificación OMS es Obesidad Grado III")

