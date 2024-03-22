##se recomienda no usar más de 3 ciclos anidados

#tabla del 5
#en el while se repite eternamente hasta que s ecumpla la condicion especifica
#en el for se conoce el rango de itirenancia

for numero in range(1,11): #1-10
    print(f"5 * {numero} = {5 * numero}")
print("")

for tabla in range(1,11):
    print(f"Tabla del numero {tabla}\n")

    for numero in range(1,11):
        print(f"{tabla} * {numero} = {tabla * numero}")
    print("")    












