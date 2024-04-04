import requests

url = "https://reqres.in/api/users"

payload = ({
    "name": "Ignacio",
    "job": "Profesor"
})

created_user = requests.post(url, json=payload)

#verificamos si quedó válido
if created_user.status_code == 201:
    print("Inserción exitosa")
    print(created_user.text)

else:
    print("Error en la creación del post")
