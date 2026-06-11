import os
from dotenv import load_dotenv 
from pprint import pprint

from pylerity import Api, User, Group
import json 


import requests


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)


all_nodes = api.nodes.get_all()

print(all_nodes[0].id)