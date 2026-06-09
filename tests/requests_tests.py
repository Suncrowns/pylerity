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

# user = api.user.get_by_id("admin")
# pprint(user.id)


user = User(
    userId="test3", enabled=True, expireAt="2026-12-31T23:59:59.000Z", groups=["6a256e63f82ad772acc0a9dc"], username="test3"
)
result = api.user.create(user)
pprint(result)


