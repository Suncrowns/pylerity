from pylerity import User, Api 
from datetime import datetime
from dotenv import load_dotenv 
from pprint import pprint
import os 


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")
print(API_KEY)


api = Api(addr=DOMAIN, api_key=API_KEY)


user1 = User(
        userId="user-12",
        username="john_doe",
        enabled=True,
        trafficLimit=1073741824,  
        groups=[],
        expireAt="2026-12-31T23:59:59"
    )
# try:
#     api.user.add(user1)
# except:
#     pass
new_user = api.user.get_by_id(user1.user_id)

new_user.username = "john Doe"
# new_user.expireAt = datetime.now()
updated_user = api.user.update(new_user)
print(updated_user)