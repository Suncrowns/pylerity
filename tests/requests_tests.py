import os
from dotenv import load_dotenv 
from pprint import pprint

from pylerity import CelerityApi



load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = CelerityApi(addr=DOMAIN, api_key=API_KEY)
stats = api.stats
pprint(stats)



