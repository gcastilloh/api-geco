import requests

# USUARIO_ANONIMO = 'usuario_anonimo'
# PASSWORD_ANONIMO = '2024anonimo'
USUARIO_ANONIMO = 'gsierram'
PASSWORD_ANONIMO = 'FalsoPassword$%'


def acortar_cadena(cadena, n):
    if len(cadena) <= n:
        return cadena  # La cadena es igual o más corta que n, no es necesario acortarla ni agregar "..."
    else:
        return cadena[:n] + "... continúa archivo"  # Agrega "..." al final de la cadena acortada

def main():
        #obtener token
        
    url_servidor = 'http://devsys.iingen.unam.mx/geco3/'

    
    url = url_servidor+'proyectos/apidocs/get-token'
    usuario = USUARIO_ANONIMO
    password = PASSWORD_ANONIMO


    # obtiene el token para trabajar con token

    data = {
          'username': usuario,
          'password': password,
      }
    response = requests.post(url, data=data)
    print(f'Response code: {response.status_code}')    

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtiene el token del cuerpo de la respuesta
        # token se utilizará como entrada a los proyectos donde se tiene derechos
        token = response.json().get('token')
        print('Proceso exitoso!')
        print(f"Token de acceso: {token}")
    else:
        print(f'Error: {response.status_code}')

    # obtiene la lista de los corpus que son públicos:
    
    url = url_servidor+'proyectos/apidocs/corpus/publicos'            # url
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    print(url)
    print(headers)
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:                # la consulta salió bien
      JSONdocsCorpus = response.json()             # obtiene los corpus en formato json
      print('-'*50)
      print('corpus publicos:')
      print(JSONdocsCorpus)
      print('-'*50,'\n'*2)
    else:
      print(f'Error: {response.status_code}')

    # obtiene la lista de los corpus en los que colabora :
    
    url = url_servidor+'proyectos/apidocs/corpus/colabora'            # url
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:                # la consulta salió bien
      JSONdocsCorpus = response.json()             # obtiene los corpus en formato json
      print('-'*50)
      print('corpus en los que colabora:')
      print(JSONdocsCorpus)
      print('-'*50,'\n'*2)
    else:
      print(f'Error: {response.status_code}')
    

    # usamos el corpus de las sexualidades como ejemplo (su id es 4)
    id_corpus = 4
    url = url_servidor+f'proyectos/apidocs/corpus/{id_corpus}'
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:                # la consulta salió bien
      JSONdocsCorpus = response.json()             # obtiene la lista de documentos del corpus en formato json
      print('-'*50)
      print('Archivos que contiene el corpus:')
      print(JSONdocsCorpus)
      print('-'*50,'\n'*2)
    else:
      print(f'*Error: {response.status_code}')

    # obtenemos un documento dentro de sexualidad 
    # por ejemplo el primer documento del listado
      
    print(f'Obtenemos el documento {JSONdocsCorpus["data"][0]}')
      
    id_doc = JSONdocsCorpus['data'][0]['id']
    url = url_servidor+f'proyectos/apidocs/corpus/{id_corpus}/{id_doc}'
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:                # la consulta salió bien
      JSONdocsCorpus = response.json()             # obtiene la lista de documentos del corpus en formato json
      print('-'*50)
      print(f'documento {id_doc}')
      print(JSONdocsCorpus)
      print('-'*50,'\n'*2)
    else:
      print(f'Error: {response.status_code}')    

    # obtenemos los metadatos de un documento dentro de sexualidad 
    # por ejemplo el primer documento cuyo id lo obtuvimos anteriormente
      
      
    url = url_servidor+f'proyectos/apidocs/corpus/{id_corpus}/{id_doc}/meta'
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:                # la consulta salió bien
      JSONdocsCorpus = response.json()             # obtiene la lista de documentos del corpus en formato json
      print('-'*50)
      print(f'metadatos del documento {id_doc}')
      print(JSONdocsCorpus)
      print('-'*50,'\n'*2)
    else:
      print(f'Error: {response.status_code}')   

    # obtenemos el  Part Of Speech (POS)  de un documento dentro de sexualidad 
    # por ejemplo el primer documento cuyo id lo obtuvimos anteriormente
      
      
    url = url_servidor+f'proyectos/apidocs/corpus/{id_corpus}/{id_doc}/pos'
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:                # la consulta salió bien
      JSONdocsCorpus = response.json()             # obtiene la lista de documentos del corpus en formato json
      print('-'*50)
      print(f'documento etiquetado con POS {id_doc}')
      print(JSONdocsCorpus)
      print('-'*50,'\n'*2)
    else:
      print(f'Error: {response.status_code}')   

    # obtenemos los documentis adjuntos de un documento dentro de sexualidad 
    # por ejemplo el primer documento cuyo id lo obtuvimos anteriormente
      
      
    url = url_servidor+f'proyectos/apidocs/corpus/{id_corpus}/{id_doc}/adjuntos'
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:                # la consulta salió bien
      JSONdocsCorpus = response.json()             # obtiene la lista de documentos del corpus en formato json
      print('-'*50)
      print(f'documentos adjuntos {id_doc}')
      print(JSONdocsCorpus)
      print('-'*50,'\n'*2)
    else:
      print(f'Error: {response.status_code}')   

    #el documento 896 de sexualidad tiene documentos adjuntos

    id_doc = 685 
    url = url_servidor+f'proyectos/apidocs/corpus/{id_corpus}/{id_doc}/adjuntos'
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:                # la consulta salió bien
      JSONdocsCorpus = response.json()             # obtiene la lista de documentos del corpus en formato json
      print('-'*50)
      print(f'documentos adjuntos {id_doc}')
      print(JSONdocsCorpus)
      print('-'*50,'\n'*2)
    else:
      print(f'Error: {response.status_code}')   


    #obtiene el documento adjunto del documento cuyo id proyecto y id se proporciona 
    # -todos los archivos adjunto se consideran binarios


    id_doc = 685 
    id_doc_adjunto = 5
    url = url_servidor+f'proyectos/apidocs/corpus/{id_corpus}/{id_doc}/adjunto/{id_doc_adjunto}'
    headers = {'Authorization': 'Token ' + token}  # token de acceso, siempre se tiene que proporcionar   
    response = requests.get(url, headers=headers ) # hace la solicitud
    if response.status_code == 200:  # la consulta salió bien
        # Define el nombre del archivo en el que quieres guardar el contenido
        content_disposition = response.headers.get('Content-Disposition')
        if content_disposition:
            nombre_archivo = content_disposition.split('filename=')[-1].strip("\"'")
        else:
            # define un nombre predeterminado si no se encuentra el nombre del archivo
            nombre_archivo = f'documento_adjunto_{id_doc_adjunto}.bin'

        # Abre un archivo en modo binario de escritura para guardar los datos
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)

        print('-' * 50)
        print(f'documento adjunto {id_doc_adjunto} guardado como {nombre_archivo}')
        print('-' * 50, '\n' * 2)
    else:
        print(f'Error: {response.status_code}')

        

if __name__ == '__main__':
   main()
