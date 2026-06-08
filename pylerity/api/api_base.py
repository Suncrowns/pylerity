import requests


class ApiFields:
    api_destination = "/api"


class BaseApi:
    def __init__(self, addr: str, api_key: str):
        self.addr = addr 
        self.api_key = api_key