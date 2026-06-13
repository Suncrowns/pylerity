import os
from dotenv import load_dotenv 
from pprint import pprint
from pylerity import Api, Group


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)

group1 = Group(
        name="premium-users",
        active=True,
        color="#FF5733",
        description="Премиум пользователи с полным доступом",
        maxDevices=10,
        subscriptionTitle="Premium"
    )


new_group = api.group.add(group1)
print(new_group)