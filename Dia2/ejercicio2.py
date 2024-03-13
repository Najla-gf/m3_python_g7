#division de enteros resulta en float
print(100/20)
print(10 + 3.5)
print(10 - 3.5)
print(10 * 3.5)

#STRING ---> cadena de caracteres
nombre= "najla"
print(nombre)
print("hagdfahfsdgha 175362refsadsag")
edad= "31"
print(edad)
print("tu edad es "+edad)

#Duplicacion
print(3*edad) #edadedadedad
numero=100
print(type(numero)) #<class 'int'>
print(3*numero)#300

#metodo count()
print("kakaroto".count("roto"))
print(len("18.198.943-2"))

#metodo upper() mayuscula y lower() minuscula
print("kAkArOtO".upper()) #KAKAROTO
print("KaKaRoTo".lower()) #kakaroto
print("KaKARTOTo".title()) #Kakaroto

#join ---> unir elementos separados
print(", ".join(["a","b","c"]))
print("".join(["a","b","c"]))
print("-".join(["a","b","c"]))

#Tipo de Datos
entero = 7
decimal = 9.5
cadena = " esto es una cadena "
booleanos = True #True or False

print(type(entero)) #<class 'int'>
print(type(decimal)) #<class 'float'>
print(type(cadena)) #<class 'str'>
print(type(booleanos)) #<class 'bool'>

#asignacion
numero2 = 200
#reasignacion
numero2 = numero2 + 100 #200 + 100

texto = "asd"
texto = texto + "qwe" #asdqwe

#precisión de datos
promedio = (4+5+7)/3
print(f"el promedio es {promedio}") #5.333333333333333
print(f"resulta de la division {promedio:.4f}") #5.3333
print(f"resulta de la division {round(promedio,3)}") #5.333

promedio = (4+6+7)/3
print(f"el promedio es {promedio}") #5.666666666666667
print(f"resulta de la division {promedio:.4f}") #5.6667
print(f"resulta de la division {round(promedio,3)}") #5.667

#ingreso de datos (INPUT)
nombre = input("Ingrese su nombre: \n")
print(f"Tu nombre es {nombre}")
edad = input("Ingrese su edad: \n")
print(f"Tu edad es {edad}")
print(type(edad))