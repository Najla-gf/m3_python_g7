def sumar(numero1, numero2):
    suma = numero1 + numero2
    return suma

#invocar funcion
sumar(14,15)
print(sumar(14,15)) #29

#imprimir el valor de retorno
print(sumar(15,16)) #31
#"Imprimir" se refiere a la acción de mostrar información en la salida estándar, que generalmente es la consola o la terminal.

#capturar el valor de retorno
valor_retorno = sumar(16,17)
print(valor_retorno)
#"capturar valores" se utiliza para recoger datos proporcionados por el usuario u otras fuentes para su posterior manipulación en el programa.
#RETORNO: devolver un valor para que pueda ser utilizado posteriormente

#ARGS=permite recoger variables sin nombre
def f(*args):
    return args
output = f (1, [2, 3], 'hola', {'clave':[4]})
print (type(output))
#<class 'tuple'>

#KWARGS= recoge argumentos con nombres, no sabemos cuantos son pero sabemos que estan identificados
def f(**kwargs):
    return kwargs
output = f(valor=1, texto='hola', lista_nombres = [4, 5, 6, 7])
print(type (output))
#<class 'dict'> 