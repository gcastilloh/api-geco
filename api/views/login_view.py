import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

def obtener_token(request):
    # Tu lógica para obtener el token aquí
    # ...

    # Luego, redirige al usuario a la URL deseada
    return redirect('corpus_disponibles')

from config import USUARIO_ANONIMO, PASSWORD_ANONIMO

from api.biblioteca import geco_url


def obtener_token(request): 
    url, headers = geco_url(request, 'proyectos/apidocs/get-token')
    if request.POST.get('anonimo'):
      print('usuario anonimo')
      usuario = USUARIO_ANONIMO
      password = PASSWORD_ANONIMO
    else:              
      print('autenticacion por user/pass')
      usuario = request.POST.get('usuario')
      password = request.POST.get('password')

    data = {
          'username': usuario,
          'password': password,
      }

    # Realiza una solicitud POST para obtener el token
    response = requests.post(url, data=data)
    print(data)
    print(f'Response code: {response.status_code}')

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtiene el token del cuerpo de la respuesta
        request.session['api_token'] = response.json().get('token')
        print(f"Token de acceso: {request.session['api_token']}")
        return redirect('corpus_disponibles')

        
    print(f'{response.status_code} Error en la autenticación. Verifica las credenciales.')

    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
    

def home(request):
    return render(request, 'index.html')
