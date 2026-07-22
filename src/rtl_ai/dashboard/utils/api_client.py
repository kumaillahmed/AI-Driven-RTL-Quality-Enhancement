import requests

def health(base_url='http://localhost:8000'):
    return requests.get(f'{base_url}/health').json()
