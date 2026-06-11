from .api_base import BaseApi, ApiFields
from pylerity.nodes import Node


class ApiNode(BaseApi):
    def __init__(self, addr, api_key):
        super().__init__(addr, api_key)

    
    def get_all(self):
        addr = self._generate_url("/nodes")
        headers = {ApiFields.api_header: self._api_key}
        req = self._get(addr, headers=headers)
        if req.status_code == 200:
            list_of_nodes = []
            for node in list(req.json()):
                node = Node.model_validate(dict(node))
                list_of_nodes.append(node)
            return list_of_nodes
        raise ValueError(f"Error {req.status_code} {dict(req.json()).get("error")}")