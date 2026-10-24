from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.data.decode("utf-8") == "OK"