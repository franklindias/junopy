from junopy.utils import get, put, post, delete


BASE_MODEL_URL = '/notifications'
WEBHOOK_BASE_MODEL_URL = f'{BASE_MODEL_URL}/webhooks'



def list_event_types():
    url = f'{BASE_MODEL_URL}/event-types'
    return get(url)

def list(params={}):
    return get(end_point=WEBHOOK_BASE_MODEL_URL, data=params)

def create(params):
    return post(end_point=WEBHOOK_BASE_MODEL_URL, data=params)

def detail(webhook_id):
    return get(end_point=f'{WEBHOOK_BASE_MODEL_URL}/{webhook_id}')

def update(webhook_id, params):
    return patch(end_point=f'{WEBHOOK_BASE_MODEL_URL}/{webhook_id}', data=params)

def delete(webhook_id):
    return delete(end_point=f'{WEBHOOK_BASE_MODEL_URL}/{webhook_id}')