import requests
import json


def request_get(url):
    return json.loads(requests.get(url).text)



######Verificación:
if __name__ == '__main__':
    response = request_get('https://aves.ninjas.cl/api/birds')
    print(response)

response = requests.get('https://aves.ninjas.cl/api/birds')
print("")
if response.status_code == 200:
    print(response)
    print("Solicitud exitosa")
else:
    print("Error en la solicitud. Código:", response.status_code)
