#Crea un diccionario
colores= {
    "Azul": "Blue",
    "Rojo": "Red",
    "Amarillo": "Yellow",
    "Verde": "Green",
    }
print(colores) #{'Azul': 'Blue', 'Rojo': 'Red', 'Amarillo': 'Yellow', 'Verde': 'Green'}

#Agrega un elemento
colores["Naranjo"] = "Orange"
print(colores) #{'Azul': 'Blue', 'Rojo': 'Red', 'Amarillo': 'Yellow', 'Verde': 'Green', 'Naranjo': 'Orange'}

#Cambia un elemento
colores["Naranjo"] = "ORANGE"
print(colores) #{'Azul': 'Blue', 'Rojo': 'Red', 'Amarillo': 'Yellow', 'Verde': 'Green', 'Naranjo': 'ORANGE'}

#Elimina un elemento
del colores["Naranjo"]
print(colores) #{'Azul': 'Blue', 'Rojo': 'Red', 'Amarillo': 'Yellow', 'Verde': 'Green'}
