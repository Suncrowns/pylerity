from datetime import datetime 
from pylerity.user import User
from .api_base import BaseApi, ApiFields


class ApiUser(BaseApi):
    def __init__(self, addr, api_key):
        super().__init__(addr, api_key)


    @property
    def addr(self):
        return self._addr
    

    @addr.setter
    def addr(self, value: str):
        self._addr = value
    

    def get_by_id(self, userId: str):
        addr = self._addr + ApiFields.api_destination + f"/users/{userId}"
        headers = {ApiFields.api_header: self._api_key}
        result = self._get(addr=addr, headers=headers)
        if result.status_code == 200:
            user = User.model_validate(dict(result.json()))
            return user
        return result.status_code, result.json()
    

    def create(self, user: User):
        addr = self._addr + ApiFields.api_destination + f"/users"
        headers = {ApiFields.api_header: self._api_key, ApiFields.accept_header: ApiFields.post_value, ApiFields.content_type_header: ApiFields.post_value}
        data = user.model_dump()
        filtered_data = {k: v for k, v in data.items() if v is not None}
        print(filtered_data)
        result = self._post(addr=addr, data=filtered_data, headers=headers)
        if result.status_code == 200:
            user = User.model_validate(dict(result.json()))
            return user
        return result.status_code