import requests, json

url = "https://jsonplaceholder.typicode.com/posts/100"

response = requests.get(url)
print("")
print(response)

#para consultar por un elemento en particular
if response.status_code == 200:
    print(response.text) #Convierte la respuesta en un string
    respuesta = json.loads(response.text)
    print(type(respuesta)) #<class 'dict'>
    for clave, valor in respuesta.items():
        print(f"clave {clave} - valor {valor}")

#para consultar por tooodo el diccionario
if response.status_code == 200:
    print(response.text) #Convierte la respuesta en un string
    respuesta = json.loads(response.text)
    print(type(respuesta)) #<class 'list'>
    for posicion, dicc in enumerate(respuesta):
        print(f"diccionario{posicion} {dicc}")