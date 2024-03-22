"""
Grupo1:
Felipe Arias
Najla Gatica
Lolett Llanquinao
Jimena Traipe
"""

#Actividad 2 - Primeros Auxilios
print("¡Bienvenido a la aplicación de primeros auxilios!")
print("Por favor, responde las siguientes preguntas para obtener ayuda:")

estimulos = input("¿La persona responde a estímulos? (si/no)\n").lower()
if estimulos == "si":
    print("Valorar la necesidad de traslado al hospital más cercano")
else:
    print("Despejar via aérea")
    respira = input ("¿La persona respira? (si/no)\n").lower()
    
    if respira == "si":
        print("Permitirle posición para respirar")
    else:
        print("Administrar 5 ventilaciones y llamar a la ambulancia")
        
        ambulancia = "no" #no ha llegado la ambulancia
        while ambulancia == "no":
            signos = input("¿Tiene signos vitales? (si/no)\n").lower()
            
            if signos == "si":
                print("Reevaluar signos vitales a la espera de la ambulancia")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
            
            ambulancia = input("¿Llegó la ambulancia? (si/no)\n").lower()
    
print("¡Aplicación de primeros auxilios terminada!")
