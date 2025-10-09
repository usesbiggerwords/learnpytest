import pytest
import src.rest_api


@pytest.fixture
def test_payload():
    return "/users/1"


def test_get(test_payload):
    http_status: int
    get_payload = test_payload
    http_status, get_result = src.rest_api.get(src.rest_api.api_url, get_payload)
    assert http_status != 0


def test_put(test_payload):
    http_status: int
    get_payload = test_payload
    http_status, put_result = src.rest_api.put(src.rest_api.api_url, get_payload)
    assert http_status != 0


def test_post(test_payload):
    http_status: int
    get_payload = test_payload
    http_status, post_result = src.rest_api.post(src.rest_api.api_url, get_payload)
    assert http_status != 0


def test_delete(test_payload):
    http_status: int
    get_payload = test_payload
    http_status, delete_result = src.rest_api.delete(src.rest_api.api_url, get_payload)
    assert http_status != 0
