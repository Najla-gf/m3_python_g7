import requests

url = "https://jsonplaceholder.typicode.com/posts/1"


response = requests.delete(url)

if response.status_code == 200: #PUT -> actualización exitosa 
    print("Actualización exitosa")
    print(response.text)
else:
    print("Error en la actualización del post")