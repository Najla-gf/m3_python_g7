#Actualización con método PUT
import requests

#Modificaremos al usuario numero 4
url = "https://reqres.in/api/users/4"

#Datos a ingresar
payload = {
    "name": "morpheus",
    "residence": "zion"
}

response = requests.put(url, json=payload)

if response.status_code == 200: #200 status ok actualizado
    updated_user = response.json()
    print("Usuario actualizado exitosamente:")
    print(updated_user)

else:
    print("Error al actualizar el usuario. Código", response.status_code)
