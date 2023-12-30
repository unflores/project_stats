from tests.conftest import client
import json


def test_request_example(client):
    response = client.get("/api/occurances/deploys")
    assert [['2010-10-10T00:00:00', 1]] == json.loads(response.data)
