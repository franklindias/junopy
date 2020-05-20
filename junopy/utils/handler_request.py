import json
import requests

from requests.auth import HTTPBasicAuth

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

BASE_URL_SANDBOX = 'https://sandbox.boletobancario.com/api-integration'
BASE_URL_PRODUCTION = 'https://api.juno.com.br'

BASE_URL_SANDBOX_AUTH = 'https://sandbox.boletobancario.com/authorization-server/oauth/token'
BASE_URL_PRODUCTION_AUTH ='https://api.juno.com.br/authorization-server/oauth/token'

TOKEN = None
RESOURCE_TOKEN = None
CLIENT_ID = None
CLIENT_SECRET = None
BASE_URL = None
BASE_URL_AUTH = None
SANDBOX = None

def validate_response(junopy_response):
    if junopy_response.status_code in [200, 201, 204, 304]:
        try:
            return junopy_response.json()
        except:
            return junopy_response
    else:
        return error(junopy_response)


def authenticate(client_id=None, client_secret=None, resource_token=None, sandbox=False):
    global TOKEN
    global RESOURCE_TOKEN
    global CLIENT_ID
    global CLIENT_SECRET
    global BASE_URL
    global BASE_URL_AUTH
    global SANDBOX

    BASE_URL_AUTH = BASE_URL_PRODUCTION_AUTH if not sandbox else BASE_URL_SANDBOX_AUTH
    
    basic_auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.post(
        BASE_URL_AUTH, 
        data={'grant_type': 'client_credentials'},
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        auth=basic_auth
    )

    TOKEN = response.json().get('access_token', None)

    RESOURCE_TOKEN = resource_token
    CLIENT_ID = client_id
    CLIENT_SECRET = client_secret
    SANDBOX = sandbox
    BASE_URL = BASE_URL_PRODUCTION if not sandbox else BASE_URL_SANDBOX


def refresh_authentication():
    global TOKEN
    basic_auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    response = requests.post(
        BASE_URL_AUTH, 
        data={'grant_type': 'client_credentials'},
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        auth=basic_auth
    )

    TOKEN = response.json().get('access_token', None)


def get(end_point, resource_token=None, params = {}, resend=False):
    url = f'{BASE_URL}{end_point}'
    junopy_response = requests.get(url, params=params, headers=get_headers(resource_token))

    if junopy_response.status_code in [403, 401] and not resend:
        refresh_authentication()
        return get(end_point, resource_token, params, resend=True)
    
    return validate_response(junopy_response)


def post(end_point, resource_token=None, data = {}, files = {}, resend=False):
    url = f'{BASE_URL}{end_point}'
    if files:
        junopy_response = requests.post(url, data=data, files=files)
    else:
        junopy_response = requests.post(url, json=data, headers=get_headers(resource_token))
    
    if junopy_response.status_code in [403, 401] and not resend:
        refresh_authentication()
        return post(end_point, resource_token, data, files, resend=True)
    
    return validate_response(junopy_response)


def put(end_point, resource_token=None, data = {}, files = {}, resend=False):
    url = f'{BASE_URL}{end_point}'
    if files:
        junopy_response = requests.put(url, data=data, files=files)
    else:        
        junopy_response = requests.put(url, json=data, headers=get_headers(resource_token))
    
    if junopy_response.status_code in [403, 401] and not resend:
        refresh_authentication()
        return put(end_point, resource_token, data, files, resend=True)
    
    return validate_response(junopy_response)


def patch(end_point, resource_token=None, data = {}, files = {}, resend=False):
    url = f'{BASE_URL}{end_point}'
    if files:
        junopy_response = requests.patch(url, data=data, files=files)
    else:        
        junopy_response = requests.patch(url, json=data, headers=get_headers(resource_token))
    
    if junopy_response.status_code in [403, 401] and not resend:
        refresh_authentication()
        return patch(end_point, resource_token, data, files, resend=True)
    
    return validate_response(junopy_response)


def delete(end_point, resource_token=None, resend=False):
    url = f'{BASE_URL}{end_point}'
    junopy_response = requests.delete(url, headers=get_headers(resource_token))
    
    if junopy_response.status_code in [403, 401] and not resend:
        refresh_authentication()
        return delete(end_point, resource_token, resend=True)
    
    return validate_response(junopy_response)


def error(junopy_response):
    error_response = {
        "message":junopy_response.json() if junopy_response.content else 'JUNO API returned an error',
        "status_code": junopy_response.status_code,
    }
    raise Exception(error_response)


def get_headers(resource_token=None):
    header = {
        'X-Api-Version': '2',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    if TOKEN:
        header['Authorization'] = f'Bearer {TOKEN}'

    if RESOURCE_TOKEN:
        header['X-Resource-Token'] = RESOURCE_TOKEN

    if resource_token:
        header['X-Resource-Token'] = resource_token
        
    return header