import os
from dotenv import load_dotenv 
from pprint import pprint

from pylerity import Api, User, Group
from pylerity.nodes import NodeType
import json 


import requests


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)


# all_nodes = api.nodes.get_all()
# node = api.nodes.get_by_id(all_nodes[0].id)
# config = api.nodes.get_hysteria_settings(node)
# pprint(config)


user = User(
    user_id = "test6",
    enabled=True,
    expireAt="2026-12-31T23:59:59.000Z",
    username="test6"
)
api.user.add(user)