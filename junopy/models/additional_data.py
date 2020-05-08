from junopy.utils import get


def list_business_areas():
    url = '/data/business-areas'
    return get(url)

def list_banks():
    url = '/data/banks'
    return get(url)

def list_company_types():
    url = '/data/company-types'
    return get(url)