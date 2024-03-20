"""
WHILE condición:
    #código a ejecutar
"""

import getpass

password= getpass.getpass("Ingrese su contraseña: \n")

while password != "Hola Mundo":
    password = getpass.getpass("No adivinaste la contraseña, ingrese nuevamente \n")

print("\nContraseña correcta!!")
print("Fin del programa")

#Iteración de n veces
i = 0
while i < 10:
    print(f"El valor de i es: {i}")
    i = i + 1 #incremento en 1
    #i +=1 --> forma abreviada del incremento

print("Fuera del while")

###
saludo = "hola"
saludo += " mundo"
print(saludo) # hola mundo
saludo += "chao"
print(saludo) # hola mundo chao