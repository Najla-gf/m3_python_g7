#Se define el diccionario

efemerides = {'1 de enero': 'Año Nuevo',
    '27 de febrero': 'Terremoto en Chile',
    '8 de marzo': 'Día de la Mujer',
    '21 de mayo': 'Glorias Navales',
    '18 de septiembre': 'Fiestas Patrias',
    '19 de septiembre': 'Glorias del Ejercito',
    '25 de diciembre': 'Navidad'}

#Se le pide al usuario consultar la fecha mediante un input
#para resolver el problema de la busqueda por la clave exacta, modificamos las claves a minusculas y agregamos un lower al input
clave = input('Ingrese una Fecha: ').lower() 

#Imprimir el resultado del valor dentro del diccionario
#nos arroja el valor como resultado
print(f'Efemérides: {efemerides[clave]}')

