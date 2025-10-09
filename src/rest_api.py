import requests
import json

from typing import Tuple, List, Dict

api_url = "https://jsonplaceholder.typicode.com"

def get(url: str, payload: str) -> Tuple[int, str]:
    status: int = 0
    packed_url = url + payload
    response = requests.get(packed_url)
    status = response.status_code
    json_data = response.json()
    return status, json_data


def put(url: str, payload: str) -> Tuple[int, str]:
    status: int = 0
    packed_url = url + payload
    response = requests.put(packed_url)
    status = response.status_code
    json_data = response.json()
    return status, json_data


def post(url: str, payload: str) -> Tuple[int, str]:
    status: int
    packed_url = url + payload
    response = requests.post(packed_url)
    status = response.status_code
    json_data = response.json()
    return status, json_data


def delete(url: str, payload: str) -> Tuple[int, str]:
    status: int
    packed_url = url + payload
    response = requests.delete(packed_url)
    status = response.status_code
    json_data = response.json()
    return status, json_data


def pretty_print(json_data: str):
    json_object = json.loads(json_data)
    print(json.dumps(json_object, indent=4))



if __name__ == "__main__":
    get_payload = "/users/1"
    http_status: int
    http_status, get_result = get(api_url, get_payload)
    print("REST API result:")
    pretty_print(get_result)
    print("Done.")
