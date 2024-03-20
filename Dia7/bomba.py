import sys, time
#Se le denomina "argumento" a lo que se escribe en la dirección del archivo 
#Se tiene que escribir la dirección en la terminal: python Dia7/bomba.py [VALOR]
#Los argumentos son CAPTURADOS como strings

print(sys.argv) #['Dia7/bomba.py', '8']
print(sys.argv[0])
print(sys.argv[1])

i = int(sys.argv[1])

while i > 0:
    print(f"EL valor de i es {i}")
    time.sleep(1) #El tiempo de espera es 1 segundo
    i -= 1 #restando 1
    
print("BOOM!!!") #Para salir del ciclo

