from datetime import datetime 
from pylerity.user import User
from .api_base import BaseApi, ApiFields
from pylerity.utils import filter_data, validate_user, UserFilterFields


class ApiUser(BaseApi):
    def __init__(self, addr, api_key):
        super().__init__(addr, api_key)


    @property
    def addr(self):
        return self._addr
    

    @addr.setter
    def addr(self, value: str):
        self._addr = value
    

    def get_by_id(self, user_id: str):
        addr = self._generate_url(f"/users/{user_id}") 
        headers = {ApiFields.api_header: self._api_key}
        result = self._get(addr=addr, headers=headers)
        
        if result.status_code == 200:
            user = User.model_validate(dict(result.json()))
            return user
        return result.status_code, result.json()
    

    def get_all(self):
        addr = self._generate_url("/users")
        headers = {ApiFields.api_header: self._api_key}
        result = self._get(addr=addr, headers=headers)
        
        if result.status_code == 200:
            lst_of_json_users = dict(result.json())["users"]
            lst_of_users = [User.model_validate(usr) for usr in lst_of_json_users]
            return lst_of_users
        return result.status_code


    def create(self, user: User):
        addr = self._generate_url("/users")
        headers = {ApiFields.api_header: self._api_key, ApiFields.accept_header: ApiFields.post_value, ApiFields.content_type_header: ApiFields.post_value}
        
        data = user.model_dump()
        filtered_data = filter_data(data=data, fields=UserFilterFields.post_fields)
        
        result = self._post(addr=addr, data=filtered_data, headers=headers)
        if result.status_code == 201:
            user = User.model_validate(dict(result.json()))
            return user
        return result.status_code
    

    def update(self, user: User):
        addr = self._generate_url(f"/users/{user.user_id}")
        headers = {ApiFields.api_header: self._api_key}
        
        validate_result = validate_user(user)
        if isinstance(validate_result, bool):
            raise ValueError("Invalid user data (hint: try check correctly specified hwidMode)")
        user = validate_result

        data = user.model_dump()
        filtered_data = filter_data(data=data, fields=UserFilterFields.put_fields)
        print(filtered_data)
        result = self._put(addr=addr, data=filtered_data, headers=headers)
        if result.status_code == 200:
            return User.model_validate(dict(result.json()))
        return result.status_code
