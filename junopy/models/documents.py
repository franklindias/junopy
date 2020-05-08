from junopy.utils import get, put, post, delete


BASE_MODEL_URL = '/documents'

def list():
    url = f'{BASE_MODEL_URL}'
    return get(url)

def detail(document_id):
    return get(f'{BASE_MODEL_URL}/{document_id}')

def send_file(document_id, params, files):
    return post(end_point=f'{BASE_MODEL_URL}/{document_id}/files', data=params, files=files)

def send_jwe_file(document_id, params, files):
    return post(end_point=f'{BASE_MODEL_URL}/{document_id}/files', data=params, files=files)