# client.py

import requests
from session import get_token

BASE_URL = "https://api.cloudflare.com/client/v4/"

def invoke_cf(method: str, endpoint: str, data: dict = None):
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json"
    }

    url = BASE_URL + endpoint
    response = requests.request(method=method, url=url, headers=headers, json=data)

    result = response.json()
    if not result.get("success", False):
        raise Exception(result)
    return result
