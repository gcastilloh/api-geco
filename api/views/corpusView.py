import requests
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import render

from api.biblioteca import geco_url

@api_view(['GET'])
def corpus_v0_1(request):
    '''
    Obtiene los corpus 
    '''
    url, headers = geco_url(request,'proyectos/apidocs/corpus')
    response = requests.get(url, headers=headers )
    data_json = response.json()

    context = {
        'usuario' : data_json['data']['usuario'],
        'data': data_json['data']['proyectos'],
    }

    return render(request, 'corpus.html', context)