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
# stats = api.server.stats
# pprint(stats)

group = Group(
    name="testGroup",
    active=True,
    color="ffffff",
    description="123131",
    maxDevices=1,
    subscriptionTitle="penisss"
)
result = api.group.add(group)
print(result)