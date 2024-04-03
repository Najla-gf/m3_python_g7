import requests
#con el metodo POST no usamos el metodo json

url = "https://jsonplaceholder.typicode.com/posts"

payload = ({
    "userId": 1,
    "id": 1,
    "title": "titulo del ejemplo",
    "body": "esto es un ejemplo del body"
})

response = requests.post(url, json=payload)

if response.status_code == 201: #201 --> created
    print("Inserción exitosa")
    print(response.text)

else:
    print("Error en la creación del post")
