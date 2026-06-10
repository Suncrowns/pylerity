import os
from dotenv import load_dotenv 
from pprint import pprint

from pylerity import Api
from pylerity import User


import requests


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)
# stats = api.server.stats
# pprint(stats)


user = api.user.get_by_id("test2")
print(user.trafficLimit)
user.trafficLimit = 10737418240

update_result = api.user.update(user)
print(update_result)