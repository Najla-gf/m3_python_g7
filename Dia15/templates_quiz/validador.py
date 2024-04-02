def validate(opciones, eleccion):
    """
    Valida la elección del usuario.

    Args:
        opciones (list): Lista de opciones válidas.
        eleccion (str): Elección del usuario.

    Returns:
        str: Elección validada.
    """
    #Definir validación de elección
    while eleccion not in opciones:
        eleccion = input('Ingrese una opción válida: ').lower()
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
