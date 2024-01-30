from config import CONF_GECO_URL

def geco_url(request, path):
  if request.session['api_token']:
    return CONF_GECO_URL+path, {'Authorization': 'Token ' + request.session['api_token']}
  return CONF_GECO_URL+path, {}