from django.shortcuts import render
import requests

from api.biblioteca import geco_url

def acortar_cadena(cadena, n):
    if len(cadena) <= n:
        return cadena  # La cadena es igual o más corta que n, no es necesario acortarla ni agregar "..."
    else:
        return cadena[:n] + "... continúa archivo ... "  # Agrega "..." al final de la cadena acortada

def procesar(request, corpus_id):

    url, headers = geco_url(request, f'proyectos/apidocs/corpus/{corpus_id}')

    response = requests.get(url, headers=headers )
    data_json = response.json()
    data = data_json.get('data', [])
    print(data)
    for item in data:
        id_archivo = item['id']
        #obtiene el contenido del documento cuyo corpus y id se proporciona
        id = corpus_id
        doc_id = id_archivo
        #print(f'id: {id} doc: {doc_id}')
        url, headers = geco_url(request, f'proyectos/apidocs/corpus/{id}/{doc_id}')
        headers = {'Authorization': 'Token ' + request.session['api_token']}
        response = requests.get(url, headers=headers )
        JSONdocsCorpus = response.json()   
        #print(acortar_cadena(JSONdocsCorpus['data'],40))     

    # Luego, pasa el objeto Corpus a tu plantilla HTML
    context = {
        'corpus_id': corpus_id,
        'data' : data,
    }

    return render(request, 'procesar.html', context)
