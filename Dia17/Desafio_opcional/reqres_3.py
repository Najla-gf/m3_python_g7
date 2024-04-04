#??????????????????
#Update y actualización usuario

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = ({
    "name": "morpheus",
    "residence": "zion"
})

updated_user = requests.post(url, json=payload)

if updated_user.status_code == 201:
    print("Inserción exitosa")
    print(updated_user.text)

else:
    print("Error en la creación del post")

#??????????????????