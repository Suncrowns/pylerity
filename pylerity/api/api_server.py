from pylerity.api.api_base import BaseApi, ApiFields


class ApiServer(BaseApi):
    def __init__(self, addr, api_key):
        super().__init__(addr, api_key)
    
    @property
    def addr(self):
        return self._addr
    
    @addr.setter
    def addr(self, addr: str):
        self._addr = addr

    
    @property
    def stats(self):
        addr = self.addr + ApiFields.api_destination + "/stats"
        headers = {ApiFields.api_header: self._api_key}
        req = self._get(addr=addr, headers=headers)
        return req.json()