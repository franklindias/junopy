from junopy.utils import get, put, post, delete


BASE_MODEL_URL = '/charges'


def list(params={}):
    url = f'{BASE_MODEL_URL}'
    return get(url, params=params)

def create(params):
    return post(end_point=BASE_MODEL_URL, data=params)

def details(charge_id):
    url = f'{BASE_MODEL_URL}/{charge_id}'
    return get(url)

def cancel(charge_id):
    url = f'{BASE_MODEL_URL}/{charge_id}/cancelation'
    return put(end_point=url)

def update_split(charge_id):
    url = f'{BASE_MODEL_URL}/{charge_id}/split'
    return put(end_point=url)