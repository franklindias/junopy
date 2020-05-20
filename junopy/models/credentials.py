from junopy.utils import get, post, patch


BASE_MODEL_URL = '/credentials'


def public_key(resource_token):
    return get(f'{BASE_MODEL_URL}/public-key', resource_token=resource_token)