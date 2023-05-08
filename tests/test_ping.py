import json


def test_ping_func(app, client):
    res = client.get("/ping")
    assert res.status_code == 200
