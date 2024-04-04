import requests
import json
from string import Template
# ^se importa esta libreria string para poder reutilizar el f-string para las fotos

def request_get(url):
    return json.loads(requests.get(url).text)

#Aquí filtramos solo las primeras 5 fotos para que no descargue las 5mil
response = request_get('https://jsonplaceholder.typicode.com/photos')[:5]

img_template = Template('<img src="$url">')
imagen = img_template.substitute(url = 'Hola')
#Aquí nos permite crear la variable url para rellenarla con las imagenes
#print(imagen)

#Template html en python
html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Título de la Página</title>
                            </head>
                            <body>

                            <h1>Nuestra página Web</h1>

                            $body
                            
                            <p>asfdafsdasfdhafsd</p>

                            </body>
                            </html>
                        ''')
print(html_template.substitute(body = imagen))

lista_url = [elemento['url'] for elemento in response]
texto_img = ''
for url in lista_url:
    texto_img += img_template.substitute(url = url) +'\n'
print(texto_img)
#Aquí imprimimos las imágenes

html = html_template.substitute(body = texto_img)
print(html)

with open('output.html', 'w') as f:
    f.write(html)






