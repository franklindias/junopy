from junopy.utils import get, post, patch


BASE_MODEL_URL = '/credentials'


def public_key():
    return get(f'{BASE_MODEL_URL}/public-key')