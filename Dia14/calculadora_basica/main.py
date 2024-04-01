import time
import sys, os
import suma
import resta as r
from input import captura_datos

opcion = input("""Esto es una calculadora:
¿Qué operación le gustaría realizar?
1. Sumar
2. Restar
0. Salir
> """) #EL input con 3 comillas permite saltos de linea en el texto

time.sleep(2) #establece una pausa en la recoleccion de datos
clear = "cls" if sys.platform == "win32" else "clear"
os.system(clear) #limpia la consola segun el sistema operativo

if opcion == '1':
    x, y = captura_datos() # 3ra forma de importar
    suma.sumar(x,y) # 1era forma de importar
elif opcion == '2':
    x, y = captura_datos() # 3ra forma de importar
    r.restar(x,y) # 2da forma de importar
elif opcion == '0':
    print('Nos vemos a la próxima')
    exit()#Lo que está después del exit no se visualiza
else:
    exit()
    print('No existe esta Operación')

print("Fin de la calculadora básica")