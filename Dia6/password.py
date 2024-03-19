#Crear script para ingresar password
#que tenga un largo minimo de 6 caracteres

import getpass #ayuda a que no se muestre la contraseña en la terminal, se oculta
#password = input("Ingrese su contraseña: ")

password = getpass.getpass("INgrese su contraseña: ")

if len(password)<6:
    print("El password es demasiado corto")







