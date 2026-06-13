import os
from dotenv import load_dotenv 
from pprint import pprint
from pylerity import Api, Node


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)



node1 = Node(
        name="node-russia-1",
        type="hysteria",  # string формат
        cascadeRole="standalone",  # string формат
        comment="Сервер в России",
        country="RU",  # 2-буквенный ISO код
        domain="server1.example.com",
        groups=["default", "russia"],
        ip="192.168.1.100",
        port=443,
        portRange="443-443",
        maxOnlineUsers=1000,
        rankingCoefficient=100
    )

all_nodes = api.nodes.get_all()
node1 = api.nodes.get_by_id(all_nodes[0].id)

print(api.nodes.get_hysteria_settings(node1))