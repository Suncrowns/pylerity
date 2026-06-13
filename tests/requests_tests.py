import os
from dotenv import load_dotenv 
from pprint import pprint

from pylerity import Api, User, Group, Node 
from pylerity.nodes import NodeType
import json 


import requests


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)


all_groups = api.group.list_groups()
print(all_groups)