"""
Grupo1:
Felipe Arias
Najla Gatica
Jimena Traipe
Lolett Llanquinao
"""

#Primeros Auxilios
print("¿Necesita ayuda? responda estas preguntas para ayudarle en su problema\n")
#usuario ingresa opción
opcion_usuario = input("¿La persona responde a estímulos?\n")
print(opcion_usuario)
if  opcion_usuario.lower() == "si":
    print("Diríjase al hospital más cercano")
elif opcion_usuario.lower() == "no":
    print("Verificar que las vías aéreas no estén obstruidas\n")
else:
    print("FIN se murió")


opcion_usuario = input("¿Está respirando?\n")
if opcion_usuario.lower() == "si":
    print("Darle espacio a la persona para que pueda respirar")
elif opcion_usuario.lower() == "no":
    print("Administrar 5 ventilaciones y llamar a la ambulancia")

while True:
    opcion_usuario = input("¿Signos de vida?\n")
    if opcion_usuario.lower() == "si":
        print("Reevaluar signos vitales a la espera de la ambulancia")
    elif opcion_usuario.lower() == "no":
        print("Administrar compresiones torácicas hasta que llegue la ambulancia")


    opcion_usuario = input("¿Llegó la ambulancia?\n")
    if opcion_usuario.lower() == "si":
        print("FIN del programa")
    
    
