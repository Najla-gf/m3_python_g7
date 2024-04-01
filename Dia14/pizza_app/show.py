#Muestra todos los ingredientes

def mostrar_ingredientes(ingredientes):
    print(f'Su masa es: {ingredientes["masa"]}')
    print(f'Su salsa es: {ingredientes["salsa"]}')
    print('Los ingredientes de su Pizza:')
    
    for ing in ingredientes['ingredientes']:
        print(f'- {ing}')

#Esta funcion muestra el tipo de masa y salsa
#Además de todos los ingredientes agregados antecedidos por un guión (-)

if __name__ == '__main__':
    ingredientes_prueba = {'masa': 'Masa Tradicional',
                        'salsa': 'Salsa de Tomate',
                        'ingredientes': ['Queso']
                        }
    mostrar_ingredientes(ingredientes_prueba)