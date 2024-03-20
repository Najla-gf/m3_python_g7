#CONDICIONAL IF
"""
Si se cumple la condicion, entonces se ejecuta el código

IF condicion:
    #código a ejecutar si es verdadero

ELIF: otra condición
    #Código a ejecutar si la primera no se cumple

ELSE: se aplica por default cuando la condición NO se cumple

"""

edad = int(input("Ingrese su edad:\n"))
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")   

print("\n") #no tiene valor, solo para generar un espacio en la terminal

if edad == 0:
    print("La edad es cero")
elif edad%2 == 0:
    print("La edad es par")
else:
    print("La edad es impar")



print("Fin del programa") #Tener cuidado con la tabulación, si está tabulado se considera dentro del IF





