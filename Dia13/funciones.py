#Definición de funciones
#Se tabula TODO lo que va dentro dela función
def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

#No sacamos nada con poner una función si no la utilizamos (invocamos), solo queda como código muerto
#Se puede invocar una función SOLO después de haberla definido.
#Las funciones se invocan al principio del codigo (buena práctica)

#DRY: DON'T REPEAT YOURSELF
#En vez de escribir un trozo de codigo 2 o + veces, es mejor crear una función

def imprimir_respuestas():
    """print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
    print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
    print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')"""
    #también se puede con un for:
    """for i in range(len(respuestas)): #[0,1,2] Len si es que no sabemos el total de preguntas
        print(f'La respuesta a la pregunta {i+1} fue {respuestas[i]}')"""
    #también se puede con ENUMERATE
    for posicion, respuesta in enumerate(respuesta):
        print(f'La respuesta a la pregunta {posicion+1} fue {respuestas}')



preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2','Enunciado Pregunta 3']
respuestas = []
# Hacer preguntas
for pregunta in preguntas: #singular dentro del plural
    print(pregunta)
    #llamado o invocación:
    imprimir_menu()
    respuestas.append(input('> '))
    print("")

imprimir_respuestas()

print('Muchas gracias por responder la encuesta')