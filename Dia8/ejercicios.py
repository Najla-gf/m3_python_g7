##Filtrado

a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)

#comprehension
##[expresion1 if condicion1 else expresion2 for variable in iterable]
filtered_array2 =[a[i] for i in range(n) if a[i] >= 1000 ]
#si el if esta antes del for, DEBE haber un else
#Si solo hay un if, va después de for in range(n)
print(filtered_array2)


##Adicto a las redes
cantidad_minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]
separador =[]
for tiempo in cantidad_minutos:
    if tiempo < 90:
        separador.append('bien')
    else:
        separador.append('mal') 
print(separador)
# comprehension
separador2=['bien'if tiempo<90 else 'mal' for tiempo in cantidad_minutos]        
print(separador2)

#Transformando segundos a minutos
