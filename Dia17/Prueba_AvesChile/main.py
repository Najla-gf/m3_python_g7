from api_get import request_get
import template as t


def pagina_html(url):
    """Crea un sitio web que muestra información sobre aves recuperada de una API.

    Args:
        url (string): enlace de la API de donde se obtiene la informacion

    Returns:
        string: texto que representa el contenido html generado
    """
    response = request_get(url)
    texto = ''
    for aves in response:
        texto += t.aves_template.substitute(
            name_spa = aves['name']['spanish'],
            name_eng = aves['name']['english'],
            url_img = aves['images']['main'], #modificacion del nombre a url_img para no confundir con url api
        )
    return t.html_template.substitute(contenido = texto)

if __name__ == '__main__':
    aves_html = pagina_html('https://aves.ninjas.cl/api/birds')
    with open('dia17/Prueba_AvesChile/index.html', 'w', encoding='utf-8') as f:
        f.write(aves_html)
