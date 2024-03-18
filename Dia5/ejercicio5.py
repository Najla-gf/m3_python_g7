edad= 27

#¿Juan es mayor de edad?
print(edad >= 18) #True
print(edad < 18) #False

#¿Juan se graduó del colegio antes de los 18 años?
edad_graduacion_colegio= 17
print(edad_graduacion_colegio < 18) #True
print(edad_graduacion_colegio == 18) #False // Por si sola no sirve para validar la informacion
print(edad_graduacion_colegio > 18) #False // Por si sola no sirve para validar la informacion
print(edad_graduacion_colegio >= 18) #False // Esta sí porque están las 2 incluidas


#¿Juan NO tiene 4 años de experiencia laboral?
experiencia_laboral= 4
print(experiencia_laboral != 4) #False
print(experiencia_laboral == 4) #True
print(experiencia_laboral < 4 or experiencia_laboral > 4) #False


#¿Juan tiene hijos?
numero_hijos= 0
print(numero_hijos > 0) #False
print(numero_hijos < 1) #True
print(numero_hijos == 0) #True
print(numero_hijos != 0) #False != distinto de

#Comparacion entre = y ==
nombre= "Najla" #Se recomienda no aplicar espacio al momento de asignar las variables
me_llamo_juan= nombre == "Juan" #Falso

nombre= "Juan"
me_llamo_juan= (nombre == "Juan") #True

"""
Edad > 18 y duracion_pololeo > 0

P = edad > 18
Q = duracion_pololeo > 0
R = 

p = T ; p = F
q = T ; q = F
r = T ; r = F

cantidad de combinaciones
2^2= 4
2^3= 8

y (and) -----> se deben cumplir AMBAS condiciones

P   Q   AND ---> si las dos son verdaderas, el resultado tambien
V   V =  V ***
V   F =  F
F   V =  F
F   F =  F

-----------------------------
o (OR) ---> cuando ambas son falsas, TODO el resultado es FALSO

P   Q   OR
V   V =  V 
V   F =  V
F   V =  V
F   F =  F ***

"""

#Soy estudiante (T) y ingreso a clases todos los días (F)
# Falsa, porque ingresamos solo de lunes a viernes. para que sea verdadera, ambas deben ser True.


#me gusta comer fruta o me gusta comer verduras
#True or True ---> True
#True or False ---> True
#False or False ---> False

#Ser o no ser
#True or False -----> True
#False or True ---> True

