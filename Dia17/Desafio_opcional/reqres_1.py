"""
Grupo1:
Felipe Arias
Najla Gatica
Lolett Llanquinao
Jimena Traipe
"""
#Solicitar info de los usuarios
import requests

url = "https://reqres.in/api/users"

#Metodo GET en API
response = requests.get(url)

#Comprobar si la peticion fue exitosa
if response.status_code == 200:
    users_data = response.json()
    print(users_data)

else:
    print("Error al obtener los datos de los usuarios. Código de error:", response.status_code)

