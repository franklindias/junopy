from junopy.utils import get, put, post, delete


BASE_MODEL_URL = '/balance'


def detail():
    return get(BASE_MODEL_URL)