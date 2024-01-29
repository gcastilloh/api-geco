@api_view(['GET'])
def corpus_v0_1(request):
    '''
    Obtiene los corpus que son públicos, no requiere autenticación para ello
    '''
    id = 4
    doc_id = 1062

    #url = CONF_GECO_URL+'proyectos/apidocs/get-token'Ì
    # print(JSONtoken)
    JSONtoken = {'token':'c51ff1be61b99259fd2f29730c6276f95944287e'}
    headers = {'Authorization': 'Token ' + JSONtoken["token"]}

    #obtener corpus publicos a partir del token con token
    url = CONF_GECO_URL+'proyectos/apidocs/corpus/publicos'
    print(url)
    response = requests.get(url, headers=headers )

    JSONdocsCorpus = response.json()
    print(response)
    return JsonResponse({'status':200,'info': response.json()}, safe=False)