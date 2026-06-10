from pylerity.groups import Group
from pylerity.utils import GroupFilterFields, filter_data
from .api_base import BaseApi, ApiFields



class ApiGroup(BaseApi):
    def __init__(self, addr, api_key):
        super().__init__(addr, api_key)
    

    @property
    def addr(self):
        return self._addr 
    

    @addr.setter
    def addr(self, value: str):
        self._addr = value 
        return self._addr 
    

    def list_groups(self):
        addr = self._generate_url("/groups")
        headers = {ApiFields.api_header: self._api_key}
        req = self._get(addr, headers=headers)
        if req.status_code == 200:
            group_list = []
            for group in list(req.json()):
                _group = Group.model_validate(group)
                group_list.append(_group)
            return group_list
        raise ValueError(f"Error {req.status_code} {dict(req.json()).get('error')}")
    

    def add(self, group: Group):
        addr = self._generate_url("/groups")
        headers = {ApiFields.api_header: self._api_key}
        data = group.model_dump()
        filtered_data = filter_data(data, GroupFilterFields.post_fields)
        req = self._post(addr, filtered_data, headers=headers)

        if req.status_code == 201:
            return True 
        raise ValueError(f"Error {req.status_code} {dict(req.json()).get('error')}")
    

    