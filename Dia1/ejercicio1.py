#comentario de una linea
"""
                varias 
    lineas de 
    comentario
    no se ve en la terminal
"""

print("Trabajando en vscode")

print(2+2)
print(10-2)
print(2*2)
print(16/8)

numero = 23
print(numero)

#LIMITANTES DE PYTHON
# NO PERMITE SUMAR LETRAS Y NUMEROS
# print("texto"+12) #TypeError: can only concatenate str (not "int) to str
print("texto",12)
#concatenar = "texto"+12
print("texto"+"34")

#INTERPOLACION
print(f"el numero es {numero}")
nombre = "Najla"
print (f"Tu nombre es {nombre} y tu edad {numero}")

print ("tu nombre es "+nombre) #concatenación
#string.format
print("Tu nombre es {} y tu edad es {}".format(nombre,numero))
# formato con %: %s para string y %d para numeros (mas antigua)
print("Tu nombre es %s y tu edad es %d" % (nombre,numero))
#metodo con cadena
apellido = "gatica fierro"
print(apellido.title())