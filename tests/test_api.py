from api import login_endpoint

def test_login_success():
    assert login_endpoint({"username": "admin", "password": "secret"}).get("status") == 200

def test_login_unauthorized():
    assert login_endpoint({"username": "admin", "password": "wrong"}).get("status") == 401

def test_login_missing_fields():
    assert login_endpoint({"username": "admin"}).get("status") == 400
