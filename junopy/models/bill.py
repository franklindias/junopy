from junopy.utils import post


BASE_MODEL_URL = '/bill-payments'


def payment(params):
    return post(BASE_MODEL_URL, data=params)