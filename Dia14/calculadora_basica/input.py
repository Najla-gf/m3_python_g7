def captura_datos():
    """Capturar los números ingresados

    Returns:
        tupla: par de números capturados
    """
    x = float(input("Ingrese el primer número"))
    y = float(input("Ingrese el segundo número"))
    return x,y #se puede retornar una tupla en python

if __name__ == "__main__": 
#esto aparecerá solo en ete script
    print("Probando el ingreso de métodos")
    print(captura_datos())