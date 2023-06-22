import requests
from circuitbreaker import circuit

from helpers.constants import DJANGO_API_URL


class DjangoAppRequestClient:
    """Request client para consumir el API del proyecto de Django"""
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }

    @circuit(failure_threshold=5, recovery_timeout=10, name='DjangoAppRequestClient.save_category')
    def save_category(self, data):
        """API para crear una categoría

        Returns:
            tuple: (response, status_code)
        """
        url = f'{DJANGO_API_URL}/categories/'

        response = requests.request("POST", url, headers={}, data=data)
        if response.status_code != 201:
            return response.json(), response.status_code

        return response.json(), response.status_code
