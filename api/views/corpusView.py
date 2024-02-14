import requests
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import render

from api.biblioteca import geco_url
from config import USUARIO_ANONIMO

@api_view(['GET'])
def corpus_v0_1(request):
    '''
    Obtiene los corpus 
    '''
    url, headers = geco_url(request,'proyectos/apidocs/corpus/publicos')
    response = requests.get(url, headers=headers )
    data_json = response.json()
    publicos = data_json['data']
    context = {}
    
    if request.session['username'] != USUARIO_ANONIMO:
      print('pedire colaboraciones')
      url, headers = geco_url(request,'proyectos/apidocs/corpus/colabora')
      response = requests.get(url, headers=headers )
      if response.status_code == 200:
        data_json = response.json()
        colabora = data_json['data']['proyectos']
        context['colabora'] = colabora
      ids_colabora = {proyecto['id'] for proyecto in colabora}
      publicos = [proyecto for proyecto in publicos if proyecto['id'] not in ids_colabora]
    context['publicos'] = publicos
    context['usuario'] = request.session['username']
    return render(request, 'corpus.html', context)