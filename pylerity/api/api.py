from.api_user import ApiUser
from .api_server import ApiServer


class Api:
    def __init__(self, addr: str, api_key: str):
        self._addr = addr 
        self._api_key = api_key
        self.server = ApiServer(
            addr=self._addr,
            api_key=self._api_key
        )
        self.user = ApiUser(
            addr=self._addr,
            api_key=self._api_key
        )

    
    @property
    def addr(self):
        return self._addr 
    

    @addr.setter
    def addr(self, value: str):
        self.server.addr = value  # без подчеркивания тк тут нормальный сеттер
        self.user._addr = value
        self._addr = value
        return value


  

    