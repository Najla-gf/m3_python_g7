import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "userId": 1,
    "title": "estamos haciendo un post con postman",
    "body": "esto es un ejemplo de post"
}


response = requests.put(url, json=payload)

if response.status_code == 200:
    updated_user = response.json()
    print("Usuario actualizado exitosamente:")
    print(updated_user)

else:
    print("Error en la actualización del post", response.status_code)