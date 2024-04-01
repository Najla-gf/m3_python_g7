def sumar(x,y):
    """Sumar dos números

    Args:
        x (float): primer numero
        y (float): segundo numero
    """
    print(f"El resultado de la suma es {x+y}")


if __name__ == "__main__": 
#lo que esté bajo esta validacion se ejecutará solo cuando se ejecute este archivo, 
#no se traslada al script main.py
    print("Probando el método")
    sumar(4,6)