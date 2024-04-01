#Opción para agregar ingredientes

#La función agregar_ingrediente() solicita los ingredientes actuales y una elección numérica.
def agregar_ingrediente(ingredientes, eleccion):

    disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo',
                'Jamón','Carne','Tocino','Queso']
    
    """#Se agrega nueva linea para validar el ingreso de los ingredientes
    eleccion_num = int(eleccion)
    if eleccion_num < 1 or eleccion_num > len(disponibles):
        print("Opción inválida. Por favor, seleccione un número válido.")
        return ingredientes"""
    
    nuevo_ingrediente = disponibles[eleccion-1] 
    #La elección numérica se utiliza como índice para identificar qué ingrediente se solicitó.

#Si el ingrediente ya existe, se devuelve un mensaje informando al usuario.
    if nuevo_ingrediente in ingredientes['ingredientes']:
        print('El ingrediente ya existe') 

#Si no existe, se agrega el ingrediente al diccionario y se informa al usuario.
    else:
        ingredientes['ingredientes'].append(nuevo_ingrediente)
        print(f'Se ha agregado {nuevo_ingrediente}')

#La función devuelve los ingredientes actualizados.
    return ingredientes

#Set de ingredientes de prueba
if __name__ == '__main__':
    ingredientes_prueba = {'masa': 'Masa Tradicional',
                        'salsa': 'Salsa de Tomate',
                        'ingredientes': ['Queso']
                        }
    #Me había faltado poner el int :B
    eleccion = int(input("""Seleccione su Ingrediente:
                    1). Tomate
                    2). Champiñones
                    3). Aceituna
                    4). Cebolla
                    5). Pollo
                    6). Jamón
                    7). Carne
                    8). Tocino
                    9). Queso
                    > """))
    ingredientes = agregar_ingrediente(ingredientes_prueba, eleccion)
    print(ingredientes)
    