from functools import lru_cache

from ..service.exceptions import InvalidLeadId
from ..app import conf
import requests


class SkorozvonAPI:
    def __init__(self) -> None:
        self.auth_url = 'https://app.skorozvon.ru/oauth/token'
        self.base_url = 'https://app.skorozvon.ru/api/v2/'

    @lru_cache(maxsize=1)
    def get_new_token(self):
        data = {
            "grant_type": "password",
            "username": conf.SKOROZVON_USERNAME,
            "api_key": conf.SKOROZVON_API_KEY,
            "client_id": conf.SKOROZVON_CLIENT_ID,
            "client_secret": conf.SKOROZVON_CLIENT_SECRET,
        }
        token = requests.post(self.auth_url, data=data).json()
        return token['access_token']
    
    def get_request(self, endpoint):
        token = {"Authorization": f'Bearer {self.get_new_token()}'}
        response = requests.get(url=self.base_url + endpoint, headers=token)
        if response.status_code == 401:
            self.get_new_token.cache_clear()
            token = {"Authorization": f'Bearer {self.get_new_token()}'}
            response = requests.get(url=self.base_url + endpoint, headers=token)
            return response.json()
        elif response.status_code == 404:
            raise InvalidLeadId("Lead ID is incorrect or missing")
        return response.json()


skorozvon_api = SkorozvonAPI()
