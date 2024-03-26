import sys

#argv nos permite ingresar informacion directamente desde la terminal
#no es muy amigable para todos porque hay que conocer bien el codigo, no es intuitivo

nombre = sys.argv[1] #esta es la ubicación 1
apellido = sys.argv[2] #esta es la ubicación 2
edad = sys.argv[3] #esta es la ubicación 3

print(f"Mi nombre es {nombre}")
print(f"Mi apellido es {apellido}")
print(f"Mi edad es {edad}")
print(f"El nombre de este archivo es {sys.argv[0]}")

print(type(sys.argv)) #se transforma en una lista y por eso podemos navegar en ella

