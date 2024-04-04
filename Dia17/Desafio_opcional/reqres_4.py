#DELETE Tracey

import requests

#Eliminar el usuario Tracey
response = requests.delete('https://reqres.in/api/users/6')

#Codigo de respuesta
print("Código de respuesta al eliminar el usuario Tracey:", response.status_code)

#Comprobar si se eliminó
if response.status_code == 204:
    print("El usuario Tracey ha sido eliminado correctamente.")
else:
    print("Error al eliminar el usuario Tracey.")