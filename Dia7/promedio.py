

##Esta forma saca el promedio de 3 notas
i = 0
suma_notas = 0
while i<3:
    nota = float(input("Ingresa tu nota:\n"))
    suma_notas = suma_notas + nota
    i += 1
    
print(f"El promedio de notas es: {suma_notas/3}")


#### OTRA FORMA
#acá se saca el promedio según la cantidad de notas que ingrese el usuario
cant_notas = int(input("ingrese cantidad de notas\n"))
i = 0
suma_notas = 0
while i < cant_notas:
    nota = float(input(f"Ingresa tu {i+1} nota\n"))
    suma_notas = suma_notas + nota
    i += 1

print(f"el promedio de notas es: {round(suma_notas/cant_notas,2)}")



