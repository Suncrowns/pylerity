import requests
from typing import Callable


class ApiFields:
    api_destination = "/api"
    api_header = "X-API-Key"
    content_type_header = "Content-Type"
    accept_header = "accept"
    post_value = "application/json"


class BaseApi:
    def __init__(self, addr: str, api_key: str):
        self._addr = addr 
        self._api_key = api_key
        self.max_retries = 3


    def _generate_url(self, dest: str):
        dest = dest.strip("/")
        return self._addr + ApiFields.api_destination + "/" + dest

    
    def _request_with_retry(self, addr: str, method: Callable[..., requests.Response], **options) -> requests.Response:
        for retry in range(1, self.max_retries + 1):
            print(f"Trying {method.__name__.upper()} to {addr}. Attempt {retry} of {self.max_retries}")
            try:
                req: requests.Responses = method(addr, **options)
                return req
            except:
                continue
        raise TimeoutError("Request attempts are out")
    

    def _get(self, addr: str, **options):
        req = self._request_with_retry(addr, requests.get, **options)
        return req


    def _post(self, addr: str, data: dict, **options):
        req = self._request_with_retry(addr, requests.post, json=data, **options)
        return req 
    

    def _put(self, addr: str, data: dict | None = None, **options):
        req = self._request_with_retry(addr, requests.put, json=data, **options)
        return req


    def _delete(self, addr: str, **options):
        req = self._request_with_retry(addr, requests.delete, **options)
        return req 
    
