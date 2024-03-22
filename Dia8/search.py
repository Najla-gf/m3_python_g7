import sys, random

numero_buscar = int(sys.argv[1])

lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista) #desordena la lista permanentemente
print(lista)

for posicion, numero in enumerate(lista):
    if numero_buscar == numero:
        print("Numero encontrado!")
        print(f"El Numero {numero_buscar} se encontró en la posición {posicion}")
        break
    else:
        print(f"El número no se encuentra en la posición {posicion}")

print("Fuera del for")





