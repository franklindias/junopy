from junopy.utils import get, put, post, delete


BASE_MODEL_URL = '/balance'


def detail(resource_token):
    return get(BASE_MODEL_URL, resource_token=resource_token)