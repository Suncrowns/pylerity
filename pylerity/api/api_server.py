from pylerity.api import BaseApi, ApiFields


class ApiServer(BaseApi):
    def __init__(self, addr, api_key):
        super().__init__(addr, api_key)
    
    @property
    def addr(self):
        return self.addr