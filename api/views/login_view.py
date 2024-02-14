import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

def obtener_token(request):
    # Tu lógica para obtener el token aquí
    # ...

    # Luego, redirige al usuario a la URL deseada
    return redirect('corpus_disponibles')

from config import USUARIO_ANONIMO, PASSWORD_ANONIMO, CONF_GECO_URL

from api.biblioteca import geco_url


def obtener_token(request): 
    if request.POST.get('anonimo'):
      usuario = USUARIO_ANONIMO
      password = PASSWORD_ANONIMO
    else:              
      usuario = request.POST.get('usuario')
      password = request.POST.get('password')


    url = CONF_GECO_URL+'proyectos/apidocs/get-token'
    data = { 'username': usuario,
             'password': password,
        }

    # Realiza una solicitud POST para obtener el token
    response = requests.post(url, data=data)
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtiene el token del cuerpo de la respuesta
        request.session['username'] = usuario
        request.session['api_token'] = response.json().get('token')
        return redirect('corpus_disponibles')
    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
    

def home(request):
    return render(request, 'index.html')
