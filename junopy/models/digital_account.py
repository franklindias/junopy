from junopy.utils import get, post, patch


BASE_MODEL_URL = '/digital-accounts'


def detail(resource_token):
    return get(BASE_MODEL_URL, resource_token=resource_token)

def create(params):
    return post(end_point=BASE_MODEL_URL, data=params)

def update(params, resource_token):
    return patch(end_point=BASE_MODEL_URL, resource_token=resource_token, data=params)