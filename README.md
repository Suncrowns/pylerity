# Pylerity

Python SDK for [C³ CELERITY panel](https://github.com/ClickDevTech/CELERITY-panel). Work for 1.3.1 version, requiring python 3.12+. 

## Overview 

This SDK is designed to interact with the [C³ CELERITY panel](https://github.com/ClickDevTech/CELERITY-panel). It provides only synchronous methods to interract with app, in the near feature planning to add asynchronous methods. The SDK is designed to be simple as far as it possible, pydantic stricly validation and own validation functions provides flexibility and reliability. 

SDK does not support version older 1.3.1, and dont work with python lower than 3.12


## 📦 Installation

```bash
git clone https://github.com/Suncrowns/pylerity.git
cd pylerity
pip install -r requirements.txt
pip install -e .
```


## Quickstart

#### Get user by userId

```python
import os 
import dotenv 
from pylerity import Api


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)


user = api.user.get_by_id("test")
print(user.user_id)
```


#### Add user to panel

```python
import os 
import dotenv 
from pylerity import Api, User


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)


user = User(
    user_id = "test",
    enabled = True,
    expireAt = "2026-07-21T17:32:28Z",
    groups = [],
    trafficLimit = 0,
    username = "test"
)

result = api.user.add(user)
print(result)
```


#### Get hysteria settings
```python
import os
from dotenv import load_dotenv 
from pprint import pprint
from pylerity import Api, Node


load_dotenv()
DOMAIN = os.getenv("DOMAIN")
API_KEY = os.getenv("API_KEY")


api = Api(addr=DOMAIN, api_key=API_KEY)

all_nodes = api.nodes.get_all()
node1 = api.nodes.get_by_id(all_nodes[0].id)

print(api.nodes.get_hysteria_settings(node1))
```




