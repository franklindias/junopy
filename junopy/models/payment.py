from junopy.utils import get, put, post, delete


BASE_MODEL_URL = '/payments'


def create(params):
    return post(end_point=BASE_MODEL_URL, data=params)

def refund(payment_id, params):
    return post(end_point=f'{BASE_MODEL_URL}/{payment_id}/refunds', data=params)

def capture(payment_id, params):
    return post(end_point=f'{BASE_MODEL_URL}/{payment_id}/capture', data=params)

def cancel(payment_id):
    return post(end_point=f'{BASE_MODEL_URL}/{payment_id}/cancelation')