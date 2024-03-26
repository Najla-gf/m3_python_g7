mascotas = {}

mascota = {
    "nombre":"",
    "raza":"",
    "peso":0.0,
    "chip": True,
    
}

cant_mascotas = int(input("Ingrese cantidad de mascotas a ingresar"))#3

for i in range(cant_mascotas):#0,1,2

    #Recorrer un diccionario con for por default
    """for clave in mascota: #con el for se va recorriendo cada clave
        #print(clave) #nombre raza peso chip
        mascota[clave] = input(f"Ingrese {clave} de su mascota: ")
    print(mascota) #{'nombre': 'Kai', 'raza': 'perro', 'peso': '17', 'chip': 'si'}
    """

    for key in mascota.keys(): 
        #print(key)
        mascota[key] = input(f"Ingrese {key} de su mascota: ")
    print(mascota) #{'nombre': 'Kai', 'raza': 'mestizo', 'peso': '17', 'chip': 'si'}
    print("")

    #Acceder a los valores del diccionario
    for valor in mascota.values():
        print(valor) #Kai mestizo 17 si
    print("")
    for clave, valor in mascota.items():
        print(f"Clave {clave} - valor {valor}") 
        #Clave nombre - valor Kai
        #Clave raza - valor mestizo
        #Clave peso - valor 17
        #Clave chip - valor si

    mascotas[mascota["nombre"]] = mascota


print(mascotas) 
#{'Nazir': {'nombre': 'Kai', 'raza': 'mestizo', 'peso': '17', 'chip': 'si'}, 
#'Kai': {'nombre': 'Kai', 'raza': 'mestizo', 'peso': '17', 'chip': 'si'}}




