import getpass
from string import ascii_lowercase

#password = getpass.getpass("Ingresa la contraseña:").lower()
password = input("Ingresa la contraseña:").lower()

minusculas = ascii_lowercase
print(minusculas)
contador = 0

for caracter in password:
    print(caracter)
    for letra in minusculas:
        contador+=1
        if caracter == letra: 
            break

print(f"La contraseña fue forzada en {contador} intentos")