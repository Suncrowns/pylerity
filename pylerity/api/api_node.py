from .api_base import BaseApi, ApiFields
from pylerity.nodes import Node, NodeType
import yaml 
import json


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
    

    def get_by_id(self, nodeId: str):
        addr = self._generate_url(f"/nodes/{nodeId}")
        headers = {ApiFields.api_header: self._api_key}
        req = self._get(addr, headers=headers)
        if req.status_code == 200:
            return Node.model_validate(dict(req.json()))
        raise ValueError(f"Error {req.status_code} {dict(req.json()).get("error")}")
    

    def get_hysteria_settings(self, node: Node):
        if node.type != NodeType.hysteria and node.type != "hysteria":
            raise ValueError("Type of node is not hysteria")
        addr = self._generate_url(f"nodes/{node.id}/config")
        headers = {ApiFields.api_header: self._api_key}
        req = self._get(addr, headers=headers)
        if req.status_code == 200:
            yaml_data = yaml.safe_load(req.text)
            return dict(json.dumps(yaml_data))
