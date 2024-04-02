import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    #Obtener las opciones disponibles para la dificultad especificada
    global opciones
    opciones_disponibles = opciones[dificultad]
    
    #Escoger una pregunta al azar
    n_elegido = random.choice(opciones_disponibles)
    
    #Eliminar la pregunta seleccionada de las opciones disponibles
    opciones_disponibles.remove(n_elegido)
    
    #Obtener la pregunta seleccionada y mezclar sus alternativas
    pregunta = preguntas[f"pregunta_{n_elegido}"]
    alternativas_mezcladas = shuffle_alt(pregunta)

    return pregunta['enunciado'], alternativas_mezcladas


if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')