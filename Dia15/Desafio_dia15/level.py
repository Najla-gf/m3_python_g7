def choose_level(n_pregunta, p_level):
    """Función para elegir el nivel de dificultad de la pregunta en función del número de pregunta y el nivel predeterminado.
    Args:
        n_pregunta (int): Número de la pregunta actual.
        p_level (int): Número máximo de preguntas por nivel.

    Returns:
        str: Nivel de dificultad de la pregunta ("básicas", "intermedias" o "avanzadas").
    """

    if n_pregunta <= p_level:  #Si el número de pregunta es menor o igual al número máximo de preguntas por nivel
        level = "basicas"
    elif n_pregunta <= 2 * p_level:  #Si el número de pregunta está entre p_level y 2 * p_level
        level = "intermedias"
    else:  #Si el número de pregunta es mayor a 2 * p_level
        level = "avanzadas"

    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(1, 1)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(9, 1)) # avanzadas
    print(choose_level(2, 1)) # intermedias
    print(choose_level(3, 1)) # avanzaas