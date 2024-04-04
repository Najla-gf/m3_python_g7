from api_get import request_get
import template as t

"""lista_url = [elemento[' url'] for elemento in out]
texto_img = ''
for url in lista_url:
            texto_img += img_template.substitute (url = url)+ '\n'
print(texto_img)"""

def pagina_html(url):
    response = request_get(url)
    texto = ''
    for aves in response:
        texto += t.aves_template. substitute(
            title_es = aves['name']['spanish'],
            title_en = aves['name']['english'],
            url = aves['images']['main'],
        )
    return t.html_template.substitute(body = texto)

if __name__ == '__main__':
    html = pagina_html('https://aves.ninjas.cl/api/birds')
    with open('dia17/index.html', 'w') as f:
        f.write(html)
