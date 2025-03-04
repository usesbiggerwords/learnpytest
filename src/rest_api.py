import requests
import json

api_url = "https://jsonplaceholder.typicode.com"

def get(url: str, payload: str) -> str:
    packed_url = url + payload
    response = requests.get(packed_url)
    json_data = response.json()
    return json.dumps(json_data)


def put(url: str, payload: str) -> str:
    return ""


def post(url: str, payload: str) -> str:
    return ""


def delete(url: str, payload: str) -> str:
    return ""


def pretty_print(json_data: str):
    json_object = json.loads(json_data)
    print(json.dumps(json_object, indent=4))



if __name__ == "__main__":
    get_payload = "/users/1"
    get_result = get(api_url, get_payload)
    print("REST API result:")
    print("Done.")
