from .api_base import BaseApi, ApiFields


class ApiNode(BaseApi):
    def __init__(self, addr, api_key):
        super().__init__(addr, api_key)

    
    def get_all(self):
        addr = self._generate_url("/nodes")
        headers = {ApiFields.api_header: self._api_key}
        req = self._get(addr, headers=headers)
        if req.status_code == 200:
            return req.json()