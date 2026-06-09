import os
from dotenv import load_dotenv 
from pprint import pprint

from pylerity import Api



load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)
# stats = api.server.stats
# pprint(stats)

user = api.user.get_by_id("admin")
pprint(user.id)


