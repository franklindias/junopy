from junopy.utils import get, post, patch


BASE_MODEL_URL = '/digital-accounts'


def list():
    return get(BASE_MODEL_URL)

def create(params):
    return post(end_point=BASE_MODEL_URL, data=params)

def update(params):
    return patch(end_point=BASE_MODEL_URL, data=params)