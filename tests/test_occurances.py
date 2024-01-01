import json

def test_occurances_returns_deploys(client):
    response = client.get("/api/occurances/deploys")
    assert [['2010-10-10T00:00:00', 1]] == json.loads(response.data)
