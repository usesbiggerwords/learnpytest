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


def test_put():
    assert False


def test_post():
    assert False


def test_delete():
    assert False
